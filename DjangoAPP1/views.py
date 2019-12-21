from django.http import HttpResponse, request
from django.shortcuts import render


def home(request):
    nome = 'Caio'
    sexo = 'f'

    lista = [
            {'nome': 'pedro', 'sexo': 'm'},
            {'nome': 'maria', 'sexo': 'f'},
            {'nome': 'roberto', 'sexo': 'm'},
    ]
    data = {'lista': lista, 'sexo': sexo, 'nome': nome }

    return render(request, 'index.html', data)



