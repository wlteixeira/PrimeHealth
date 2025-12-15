from django.shortcuts import render
import csv
from django.http import HttpResponse
from sintomas.models import Sintoma

def exportar_relatorio_csv(request):
    resposta = HttpResponse(content_type='text/csv')
    resposta['Content-Disposition'] = (
        'attachment; filename="relatorio_sintomas.csv"'
    )

    escritor = csv.writer(resposta)
    escritor.writerow(['Nome', 'Intensidade', 'Data'])

    for sintoma in Sintoma.objects.filter(usuario=request.user):
        escritor.writerow([
            sintoma.nome,
            sintoma.intensidade,
            sintoma.data_registro
        ])

    return resposta
