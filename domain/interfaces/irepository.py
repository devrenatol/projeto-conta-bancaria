from abc import ABC
from typing import TypeVar, Generic

T = TypeVar('T')

class IRepository(ABC, Generic[T]):
    def get_all(self, ordering):
        pass

    def get_by_id(self, id):
        pass

    def create(self, dictionary):
        pass

    def update(self, dictionary, id):
        pass

    def delete(self, id):
        pass