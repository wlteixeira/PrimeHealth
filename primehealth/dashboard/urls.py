from django.urls import path
from .views import painel_saude, exportar_relatorio_pdf, exportar_relatorio_csv

urlpatterns = [
    path('', painel_saude, name='painel_saude'),
    path('exportar/pdf/', exportar_relatorio_pdf, name='exportar_relatorio_pdf'),
    path('exportar/csv/', exportar_relatorio_csv, name='exportar_relatorio_csv'),
]
