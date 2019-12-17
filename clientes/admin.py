from django.contrib import admin
from .models import Clientes
from .models import Telefone
from .models import CPF
from .models import Departamento


admin.site.register(Clientes)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)

# Register your models here.
