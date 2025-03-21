from domain.interfaces import IContaBancariaRepository
from domain.entities import ContaBancaria
from data.repositories import Repository
from data.models import ContaBancariaModel
from data.mapping import ContaBancariaMapping
from dataclasses import asdict

class ContaBancariaRepository(Repository[ContaBancariaModel], IContaBancariaRepository):
    
    def __init__(self):
        super().__init__(ContaBancariaModel)

    def get_all(self, ordering):

        CAMPOS_PARA_ORDENACAO = ['account_number', 'account_holder']

        if ordering and ordering.lstrip('-') in CAMPOS_PARA_ORDENACAO:
            contas_bancarias_model = super().get_all().order_by(ordering)
            contas_bancarias_entity = [ContaBancariaMapping.to_entity(conta_bancaria) for conta_bancaria in contas_bancarias_model]

            return contas_bancarias_entity
        else:
            contas_bancarias_model = super().get_all()
            contas_bancarias_entity = [ContaBancariaMapping.to_entity(conta_bancaria) for conta_bancaria in contas_bancarias_model]

            return contas_bancarias_entity          
    
    def get_by_id(self, id: int) -> ContaBancaria:
        conta_bancaria_model = super().get_by_id(id)
        conta_bancaria_entity = ContaBancariaMapping.to_entity(conta_bancaria_model)

        return conta_bancaria_entity
    
    def create(self, dictionary: dict) -> ContaBancaria:
        conta_bancaria_entity = ContaBancariaMapping.dict_to_entity(dictionary)
        conta_bancaria_model = ContaBancariaMapping.to_model(conta_bancaria_entity)
        super().create(conta_bancaria_model)
        conta_bancaria_adicionada_entity = ContaBancariaMapping.to_entity(conta_bancaria_model)
        
        return conta_bancaria_adicionada_entity
    
    def update(self, dictionary: dict, id: int) -> ContaBancaria:
        conta_bancaria_entity = ContaBancariaMapping.dict_to_entity(dictionary)
        conta_bancaria_dict = ContaBancariaMapping.entity_to_dict(conta_bancaria_entity)
        conta_bancaria_modificada_model = super().update(conta_bancaria_dict, id)
        conta_bancaria_modificada_entity = ContaBancariaMapping.to_entity(conta_bancaria_modificada_model)

        return conta_bancaria_modificada_entity
    
    def delete(self, id: int) -> ContaBancaria:
        return super().delete(id)
