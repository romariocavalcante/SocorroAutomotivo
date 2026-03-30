from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, "index.html")


def solicitar_socorro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')
        print(f"Solicitação: {nome}, {telefone}, {veiculo}, {localizacao}, {problema}")

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_socorro.html')


def socorrista_encontrado(request):
    data = request.session.pop('last_request', {})
    return render(request, 'socorrista_encontrado.html', data)


def guincho(request):
    return render(request, 'guincho.html')


def troca_pneu(request):
    return render(request, 'troca_pneu.html')


def chaveiro_automotivo(request):
    return render(request, 'chaveiro_automotivo.html')


def recarga_bateria(request):
    return render(request, 'recarga_bateria.html')


def pane_mecanica(request):
    return render(request, 'pane_mecanica.html')


def falta_combustivel(request):
    return render(request, 'falta_combustivel.html')


def solicitar_guincho(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
            'servico': 'Guincho'
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_guincho.html')


def solicitar_troca_pneu(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
            'servico': 'Troca de Pneu'
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_troca_pneu.html')


def solicitar_chaveiro_automotivo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
            'servico': 'Chaveiro Automotivo'
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_chaveiro_automotivo.html')


def solicitar_recarga_bateria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
            'servico': 'Recarga de Bateria'
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_recarga_bateria.html')


def solicitar_pane_mecanica(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
            'servico': 'Pane Mecânica'
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_pane_mecanica.html')


def solicitar_falta_combustivel(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        veiculo = request.POST.get('veiculo')
        localizacao = request.POST.get('localizacao')
        problema = request.POST.get('problema')

        request.session['last_request'] = {
            'nome': nome,
            'telefone': telefone,
            'veiculo': veiculo,
            'localizacao': localizacao,
            'problema': problema,
            'servico': 'Falta de Combustível'
        }

        return redirect('socorrista_encontrado')

    return render(request, 'solicitar_falta_combustivel.html')