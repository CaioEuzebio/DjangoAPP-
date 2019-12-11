from django.http import HttpResponse

def home(response):
    return HttpResponse('Home')

def clientes(request):
    return HttpResponse('A')

def clientes_detalhe(request, id):
    return HttpResponse(id)