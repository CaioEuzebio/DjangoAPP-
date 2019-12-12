from django.contrib import admin
from .models import Clientes
from .models import Telefone
from .models import CPF


admin.site.register(Clientes)
admin.site.register(Telefone)
admin.site.register(CPF)

# Register your models here.
