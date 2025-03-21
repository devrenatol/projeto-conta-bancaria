from django.urls import path, include
from rest_framework import routers
from api.views import ContaBancariaView, ListaContaBancariaView
from api.views.transacao_views import SaqueView, DepositoView, TransferenciaView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('contasbancarias/', ListaContaBancariaView.as_view()),
    path('contabancaria/<int:pk>/', ContaBancariaView.as_view()),
    path('transacao/saque/<int:pk>', SaqueView.as_view()),
    path('transacao/deposito/<int:pk>', DepositoView.as_view()),
    path('transacao/transferencia/<int:pk>', TransferenciaView.as_view())
]