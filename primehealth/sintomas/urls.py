from django.urls import path
from .views import (
    listar_sintomas,
    cadastrar_sintoma,
    editar_sintoma,
    excluir_sintoma
)

urlpatterns = [
    path('', listar_sintomas, name='listar_sintomas'),
    path('novo/', cadastrar_sintoma, name='cadastrar_sintoma'),
    path('editar/<int:id>/', editar_sintoma, name='editar_sintoma'),
    path('excluir/<int:id>/', excluir_sintoma, name='excluir_sintoma'),
]
