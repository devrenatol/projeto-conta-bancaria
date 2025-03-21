from abc import ABC

class IContaBancariaService(ABC):
    def get_all(self, ordering):
        pass

    def get(self, id):
        pass

    def post(self, conta_bancaria_dict):
        pass

    def put(self, conta_bancaria_dict, id):
        pass

    def delete(self, id):
        pass