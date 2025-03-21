from abc import ABC

class ITransacaoService(ABC):
    def get(self, id):
        pass
    
    def sacar(self, id, value):
        pass

    def depositar(self, id, value):
        pass

    def transferencia(self, id, value):
        pass