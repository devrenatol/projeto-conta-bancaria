from domain.entities import ContaBancaria

class ContaBancariaApplicationMapping():

    @staticmethod
    def entity_to_dict(entity: ContaBancaria):
        return {
            'account_number': entity.account_number,
            'account_holder': entity.account_holder,
            'balance': entity.balance
        }