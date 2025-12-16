from django.urls import path
from .views import (
    listar_sinais_vitais,
    criar_sinal_vital,
    editar_sinal_vital,
    excluir_sinal_vital
)

urlpatterns = [
    path('', listar_sinais_vitais, name='listar_sinais_vitais'),
    path('novo/', criar_sinal_vital, name='criar_sinal_vital'),
    path('editar/<int:id>/', editar_sinal_vital, name='editar_sinal_vital'),
    path('excluir/<int:id>/', excluir_sinal_vital, name='excluir_sinal_vital'),
]
