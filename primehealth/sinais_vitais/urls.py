from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_sinais_vitais, name='listar_sinais_vitais'),
    path('cadastrar/', views.cadastrar_sinal_vital, name='cadastrar_sinal_vital'),
    path('editar/<int:id>/', views.editar_sinal_vital, name='editar_sinal_vital'),
    path('excluir/<int:id>/', views.excluir_sinal_vital, name='excluir_sinal_vital'),
]
