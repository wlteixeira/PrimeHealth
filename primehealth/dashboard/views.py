from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sinais_vitais.models import SinalVital
from sintomas.models import Sintoma
from medicamentos.models import Medicamento
from django.utils import timezone
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas

@login_required
def painel_saude(request):
    usuario = request.user

    sinais_vitais = SinalVital.objects.filter(usuario=usuario).order_by('-data_hora')[:5]
    sintomas = Sintoma.objects.filter(usuario=usuario).order_by('-data_hora')[:5]
    medicamentos = Medicamento.objects.filter(usuario=usuario)

    contexto = {
        'sinais_vitais': sinais_vitais,
        'sintomas': sintomas,
        'medicamentos': medicamentos,
    }

    return render(request, 'painel.html', contexto)

@login_required
def exportar_relatorio_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio_saude.csv"'

    writer = csv.writer(response)
    writer.writerow(['RELATÓRIO DE SAÚDE'])

    writer.writerow([])
    writer.writerow(['Sintomas'])
    writer.writerow(['Nome', 'Intensidade', 'Data/Hora'])

    for sintoma in Sintoma.objects.filter(usuario=request.user):
        writer.writerow([sintoma.nome, sintoma.intensidade, sintoma.data_hora])

    writer.writerow([])
    writer.writerow(['Sinais Vitais'])
    writer.writerow(['Tipo', 'Valor', 'Data/Hora'])

    for sinal in SinalVital.objects.filter(usuario=request.user):
        writer.writerow([sinal.tipo, sinal.valor, sinal.data_hora])

    return response

@login_required
def exportar_relatorio_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_saude.pdf"'

    pdf = canvas.Canvas(response)
    largura, altura = 595, 842  # A4
    y = altura - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Relatório de Saúde")
    y -= 25

    pdf.setFont("Helvetica", 10)
    data_geracao = timezone.localtime().strftime('%d/%m/%Y %H:%M')
    pdf.drawString(50, y, f"Gerado em: {data_geracao}")
    y -= 40

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Sintomas")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for sintoma in Sintoma.objects.filter(usuario=request.user):
        data_sintoma = sintoma.data_hora.strftime('%d/%m/%Y %H:%M')
        pdf.drawString(
            50,
            y,
            f"{sintoma.nome} | Intensidade: {sintoma.intensidade} | {data_sintoma}"
        )
        y -= 15

        if y < 50:
            pdf.showPage()
            y = altura - 50
            pdf.setFont("Helvetica", 10)

    y -= 20

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Sinais Vitais")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for sinal in SinalVital.objects.filter(usuario=request.user):
        data_sinal = sinal.data_hora.strftime('%d/%m/%Y %H:%M')
        pdf.drawString(
            50,
            y,
            f"{sinal.tipo} | Valor: {sinal.valor} | {data_sinal}"
        )
        y -= 15

        if y < 50:
            pdf.showPage()
            y = altura - 50
            pdf.setFont("Helvetica", 10)

    pdf.showPage()
    pdf.save()

    return response