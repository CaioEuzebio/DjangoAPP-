from django.contrib import admin
from .models import Clientes
from .models import Telefone
from .models import CPF
from .models import Departamento


class EmpregadoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_filter = [('departamentos')]
    search_fields = ('id', 'nome','email')


admin.site.register(Clientes, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)

# Register your models here.
