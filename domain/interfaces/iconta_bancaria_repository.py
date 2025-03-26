from domain.interfaces import IRepository
from domain.entities import ContaBancaria

class IContaBancariaRepository(IRepository[ContaBancaria]):
    def update_balance(self, dictionary, id):
        pass