from django.urls import path
from .views import (
    listar_medicamentos,
    cadastrar_medicamento,
    editar_medicamento,
    excluir_medicamento
)

urlpatterns = [
    path('', listar_medicamentos, name='listar_medicamentos'),
    path('novo/', cadastrar_medicamento, name='cadastrar_medicamento'),
    path('editar/<int:id>/', editar_medicamento, name='editar_medicamento'),
    path('excluir/<int:id>/', excluir_medicamento, name='excluir_medicamento'),
]
