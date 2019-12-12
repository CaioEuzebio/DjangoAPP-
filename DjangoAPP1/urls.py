"""DjangoAPP1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home
from clientes.views import clientes, clientes_detalhe, clientes_por_nome

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^clientes/(?P<id>\d{1,3})$', clientes_detalhe),
    url(r'^clientes/(?P<nome>\w+)$', clientes_por_nome),
    url(r'^clientes', clientes),
    url(r'', home)
    

]
