from domain.entities import ContaBancaria
from data.models import ContaBancariaModel

class ContaBancariaMapping():

    @staticmethod
    def to_entity(model: ContaBancariaModel):
        return ContaBancaria(
            id = model.id,
            account_number = model.account_number,
            account_holder = model.account_holder,
            balance = model.balance,
            created_at = model.created_at,
            updated_at = model.updated_at
        )
    
    @staticmethod
    def to_model(entity: ContaBancaria):
        return ContaBancariaModel(
            account_number = entity.account_number,
            account_holder = entity.account_holder,
            balance = entity.balance
        )
    
    @staticmethod
    def dict_to_entity(dictionary: dict):
        return ContaBancaria(
            account_holder = dictionary['account_holder'],
            account_number = dictionary['account_number'],
            balance = dictionary['balance']
        )
    
    @staticmethod
    def entity_to_dict(entity: ContaBancaria):
        return {
            'account_number': entity.account_number,
            'account_holder': entity.account_holder,
            'balance': entity.balance
        }