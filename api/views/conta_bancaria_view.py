from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from infra.container_di import app_injector
from application.services.interfaces import IContaBancariaService

class ContaBancariaView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service = app_injector.get(IContaBancariaService)

    def get(self, request, pk=None):
        try:
            conta_bancaria = self._service.get(id=pk)
            return Response(conta_bancaria, status=status.HTTP_200_OK)
        except:
            return Response(f'Não foi possível encontrar conta bancária de id = {pk}')
        
    def put(self, request, pk=None):
        try:
            conta_bancaria = self._service.put(conta_bancaria_dict=request.data, id=pk)
            return Response(conta_bancaria, status=status.HTTP_200_OK)
        except ValueError as error:
            if isinstance(error.args[0], dict):
                formatted_errors = {field: list(map(str, errors)) for field, errors in error.args[0].items()}
                return Response({'errors': formatted_errors}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'errors': str(error)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            conta_bancaria_is_deleted = self._service.delete(id=pk)

            if not conta_bancaria_is_deleted:
                return Response(f'Não foi possível deletar conta bancária de id = {pk}')
            
            return Response('Conta bancária deletada com sucesso!', status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Erro interno do sistema', status=status.HTTP_500_INTERNAL_SERVER_ERROR)