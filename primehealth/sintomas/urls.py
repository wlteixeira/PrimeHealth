from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_sintomas, name='listar_sintomas'),
    path('cadastrar/', views.cadastrar_sintoma, name='cadastrar_sintoma'),
    path('editar/<int:id>/', views.editar_sintoma, name='editar_sintoma'),
    path('excluir/<int:id>/', views.excluir_sintoma, name='excluir_sintoma'),
]
