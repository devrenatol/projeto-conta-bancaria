from domain.interfaces import IContaBancariaRepository
from application.services.interfaces import ITransacaoService
from application.serializers import TransacaoRequestSerializer, TransacaoResponseSerializer, ContaBancariaRequestSerializer,TransferenciaRequestSerializer
from application.application_mapping import ContaBancariaApplicationMapping
from injector import inject
from decimal import Decimal

class TransacaoService(ITransacaoService):

    @inject
    def __init__(self, conta_bancaria_repository: IContaBancariaRepository):
        super().__init__()
        self._repository = conta_bancaria_repository

    def get(self, id):
        try:
            conta_bancaria_entity = self._repository.get_by_id(id=id)
            conta_bancaria_dto = TransacaoResponseSerializer(conta_bancaria_entity)

            return conta_bancaria_dto.data
        except:
            raise ValueError('Não foi possível recuperar dados da conta bancária')
    

    def sacar(self, id, value):
        transacao = TransacaoRequestSerializer(data=value)

        if not transacao.is_valid():
            raise ValueError(transacao.errors)
        
        try:
            conta_bancaria_entity = self._repository.get_by_id(id=id)
            conta_bancaria_entity.sacar_balance(Decimal(transacao.validated_data['value']))
            conta_bancaria_dict = ContaBancariaApplicationMapping.entity_to_dict(conta_bancaria_entity)
            transacao_dto = ContaBancariaRequestSerializer(data=conta_bancaria_dict)

            if transacao_dto.is_valid():
                conta_bancaria_transacao_concluida = self._repository.update_balance(dictionary=transacao_dto.validated_data, id=id)
                conta_bancaria_transacao_concluida_dto = TransacaoResponseSerializer(conta_bancaria_transacao_concluida)

            return conta_bancaria_transacao_concluida_dto.data
        except:
            raise ValueError('Não foi possível fazer o saque')
        
    def depositar(self, id, value):
        transacao = TransacaoRequestSerializer(data=value)

        if not transacao.is_valid():
            raise ValueError(transacao.errors)
        
        try:
            conta_bancaria_entity = self._repository.get_by_id(id=id)
            conta_bancaria_entity.depositar_balance(Decimal(transacao.validated_data['value']))
            conta_bancaria_dict = ContaBancariaApplicationMapping.entity_to_dict(conta_bancaria_entity)
            transacao_dto = ContaBancariaRequestSerializer(data=conta_bancaria_dict)

            if transacao_dto.is_valid():
                conta_bancaria_transacao_concluida = self._repository.update_balance(dictionary=transacao_dto.validated_data, id=id)
                conta_bancaria_transacao_concluida_dto = TransacaoResponseSerializer(conta_bancaria_transacao_concluida)

            return conta_bancaria_transacao_concluida_dto.data
        except:
            raise ValueError('Não foi possível fazer o saque')
        
    def transferencia(self, id, value):
        transacao = TransferenciaRequestSerializer(data=value)

        if not transacao.is_valid():
            raise ValueError(transacao.errors)
        
        try:
            conta_bancaria_entity = self._repository.get_by_id(id=id)
            conta_bancaria_receptor_entity = self._repository.get_by_id(id=transacao.validated_data['id'])

            conta_bancaria_entity.sacar_balance(Decimal(transacao.validated_data['value']))
            conta_bancaria_receptor_entity.depositar_balance(Decimal(transacao.validated_data['value']))

            conta_bancaria_saque_dict = ContaBancariaApplicationMapping.entity_to_dict(conta_bancaria_entity)
            conta_bancaria_receptor_dict = ContaBancariaApplicationMapping.entity_to_dict(conta_bancaria_receptor_entity)

            transacao_saque_dto = ContaBancariaRequestSerializer(data=conta_bancaria_saque_dict)
            transacao_deposito_dto = ContaBancariaRequestSerializer(data=conta_bancaria_receptor_dict)

            if transacao_saque_dto.is_valid():
                conta_bancaria_transacao_saque_concluida = self._repository.update_balance(dictionary=transacao_saque_dto.validated_data, id=id)
                conta_bancaria_transacao_concluida_dto = TransacaoResponseSerializer(conta_bancaria_transacao_saque_concluida)
            
            if transacao_deposito_dto.is_valid():
                self._repository.update_balance(dictionary=transacao_deposito_dto.validated_data, id=conta_bancaria_receptor_entity.id)


            return conta_bancaria_transacao_concluida_dto.data
        except:
            raise ValueError('Não foi possível fazer a transferência')      