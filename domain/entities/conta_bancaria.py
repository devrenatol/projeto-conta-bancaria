from datetime import datetime
from decimal import Decimal


class ContaBancaria():

    def __init__(self, account_number: str, account_holder: str, balance: Decimal, id: int = 0, created_at: datetime = None, updated_at: datetime = None):
        self._validations(balance)
        self.account_number = account_number
        self.account_holder = account_holder
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def _validations(self, balance):
        if balance == 0:
            self.balance = balance
        else:
            balance = Decimal(balance)
            
            if balance < 0:
                raise ValueError('O saldo da conta não pode ser negativo')
            
            self.balance = balance
    

    def sacar_balance(self, value):
        if self.balance < value:
            raise ValueError('O saldo da conta não pode ser negativo')
        elif value <= 0:
            raise ValueError('O valor para saque tem que ser um numero positivo')
        
        self.balance -= value

    def depositar_balance(self, value):
        if value <= 0:
            raise ValueError('O valor de deposito tem que ser um numero positivo')
        
        self.balance += value