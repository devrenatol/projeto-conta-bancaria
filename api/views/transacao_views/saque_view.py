from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from infra.container_di import app_injector
from application.services.interfaces import ITransacaoService, IContaBancariaService

class SaqueView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service = app_injector.get(ITransacaoService)

    def get(self, request, pk=None):
        try:
            conta_bancaria = self._service.get(id=pk)
            return Response(conta_bancaria, status=status.HTTP_200_OK)
        except:
            return Response(f'Não foi possível encontrar conta bancária de id = {pk}')
    
    def post(self, request, pk=None):
        try:
            transacao_saque = self._service.sacar(id=pk, value=request.data)
            return Response(transacao_saque, status=status.HTTP_202_ACCEPTED)
        except ValueError as error:
            if isinstance(error.args[0], dict):
                formatted_errors = {field: list(map(str, errors)) for field, errors in error.args[0].items()}
                return Response({'errors': formatted_errors}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'errors': str(error)}, status=status.HTTP_400_BAD_REQUEST)
