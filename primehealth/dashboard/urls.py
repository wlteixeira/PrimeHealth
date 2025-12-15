from django.urls import path
from .views import painel_saude

urlpatterns = [
    path('', painel_saude, name='painel_saude'),
]
