from domain.interfaces import IContaBancariaRepository
from application.services.interfaces import IContaBancariaService
from application.serializers import ContaBancariaResponseSerializer, ContaBancariaRequestSerializer
from injector import inject

class ContaBancariaService(IContaBancariaService):

    @inject
    def __init__(self, conta_bancaria_repository: IContaBancariaRepository):
        super().__init__()
        self._repository = conta_bancaria_repository
    
    def get_all(self, ordering):
        try:
            contas_bancarias_entity = self._repository.get_all(ordering=ordering)
            contas_bancarias_dto = ContaBancariaResponseSerializer(contas_bancarias_entity, many=True)

            return contas_bancarias_dto.data
        except:
            raise ValueError('Não foi possível recuperar os dados das contas bancárias')
    
    def get(self, id):
        try:
            conta_bancaria_entity = self._repository.get_by_id(id=id)
            conta_bancaria_dto = ContaBancariaResponseSerializer(conta_bancaria_entity)

            return conta_bancaria_dto.data
        except:
            raise ValueError('Não foi possível recuperar dados da conta bancária')
    
    def post(self, conta_bancaria_dict):
        conta_bancaria_dto = ContaBancariaRequestSerializer(data=conta_bancaria_dict)

        if not conta_bancaria_dto.is_valid():
            raise ValueError(conta_bancaria_dto.errors)
        
        try:
            conta_bancaria_adicionada = self._repository.create(dictionary=conta_bancaria_dto.validated_data)
            conta_bancaria_adicionada_dto = ContaBancariaResponseSerializer(conta_bancaria_adicionada)

            return conta_bancaria_adicionada_dto.data
        except:
            raise ValueError('Não foi possível criar a conta bancária')
    
    def put(self, conta_bancaria_dict, id):
        conta_bancaria_dto = ContaBancariaRequestSerializer(data=conta_bancaria_dict)

        if not conta_bancaria_dto.is_valid():
            raise ValueError(conta_bancaria_dto.errors)
        
        try:
            conta_bancaria_modificada_entity = self._repository.update(dictionary=conta_bancaria_dto.validated_data, id=id)
            conta_bancaria_modificada_dto = ContaBancariaResponseSerializer(conta_bancaria_modificada_entity)

            return conta_bancaria_modificada_dto.data
        except:
            raise ValueError('Não foi possível modificar a conta bancária')

    def delete(self, id):
        try:
            conta_bancaria_is_deleted = self._repository.delete(id=id)

            if not conta_bancaria_is_deleted:
                return False
            
            return True
        except:
            raise ValueError('Não foi possível deletar a conta bancária')