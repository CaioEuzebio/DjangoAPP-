from django.http import HttpResponse

def home(response):
    return HttpResponse('Home')

def clientes(request):
    return HttpResponse('A')

def clientes_detalhe(request, id):
    return HttpResponse(id)

def clientes_por_nome(request, nome):
    return HttpResponse('Ola %s: ' % nome)