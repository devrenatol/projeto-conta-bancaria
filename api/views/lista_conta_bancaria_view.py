from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from infra.container_di import app_injector
from application.services.interfaces import IContaBancariaService

class ListaContaBancariaView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service = app_injector.get(IContaBancariaService)

    def get(self, request):
        try:
            ordering = request.query_params.get('ordering', None)
            contas_bancarias = self._service.get_all(ordering=ordering)
            
            return Response(contas_bancarias, status=status.HTTP_200_OK)
        except:
            return Response('Nenhuma conta bancária registrada', status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        try:
            conta_bancaria = self._service.post(conta_bancaria_dict=request.data)
            return Response(conta_bancaria, status=status.HTTP_201_CREATED)
        except ValueError as error:
            if isinstance(error.args[0], dict):
                formatted_errors = {field: list(map(str, errors)) for field, errors in error.args[0].items()}
                return Response({'errors': formatted_errors}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'errors': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
        
