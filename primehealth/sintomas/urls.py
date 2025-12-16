from django.urls import path
from .views import (
    listar_sintomas,
    criar_sintoma,
    editar_sintoma,
    excluir_sintoma
)

urlpatterns = [
    path('', listar_sintomas, name='listar_sintomas'),
    path('novo/', criar_sintoma, name='criar_sintoma'),
    path('editar/<int:id>/', editar_sintoma, name='editar_sintoma'),
    path('excluir/<int:id>/', excluir_sintoma, name='excluir_sintoma'),
]
