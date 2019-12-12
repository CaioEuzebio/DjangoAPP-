from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def clientes(request):
    return HttpResponse('A')

def clientes_detalhe(request, id):
    return HttpResponse(id)

def clientes_por_nome(request, nome):
    return HttpResponse(f'Ola, como você está? {nome}')