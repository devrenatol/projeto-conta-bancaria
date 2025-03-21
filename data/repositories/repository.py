from domain.interfaces import IRepository
from typing import TypeVar, Generic
from django.core.exceptions import ObjectDoesNotExist

T = TypeVar('T')

class Repository(IRepository[T], Generic[T]):

    def __init__(self, model: type[T]):
        self._model = model

    def get_all(self):
        return self._model.objects.all()

    def get_by_id(self, id: int):
        return self._model.objects.get(id=id)
    
    def create(self, entity: type[T]):
        entity.save()

    def update(self, dictionary: dict, id: int):
        try:
            model_verificado = self._model.objects.get(id=id)
        except ObjectDoesNotExist:
            raise ValueError()
        
        for key, value in dictionary.items():
            if getattr(model_verificado, key) != value:
                setattr(model_verificado, key, value)
        
        model_verificado.save()
        return model_verificado
        
    
    def delete(self, id: int):
        try:
            entity = self._model.objects.get(id=id)
        except ObjectDoesNotExist:
            return False
        
        entity.delete()
        return True