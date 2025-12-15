from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_medicamentos, name='listar_medicamentos'),
    path('cadastrar/', views.cadastrar_medicamento, name='cadastrar_medicamento'),
    path('editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('excluir/<int:id>/', views.excluir_medicamento, name='excluir_medicamento'),
]
