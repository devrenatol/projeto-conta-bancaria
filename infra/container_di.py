from injector import Module, Injector, singleton
from domain.interfaces import IContaBancariaRepository
from data.repositories import ContaBancariaRepository
from application.services.interfaces import IContaBancariaService, ITransacaoService
from application.services import ContaBancariaService, TransacaoService

class AppModule(Module):
    
    def configure(self, binder):
        binder.bind(IContaBancariaRepository, to=ContaBancariaRepository, scope=singleton)
        binder.bind(IContaBancariaService, to=ContaBancariaService, scope=singleton)
        binder.bind(ITransacaoService, to=TransacaoService, scope=singleton)

app_injector = Injector([AppModule()])