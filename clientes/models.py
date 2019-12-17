from django.db import models

# Create your models here.



class Departamento(models.Model):
    nome = models.CharField(max_length=50)

class CPF(models.Model):
    numero = models.CharField(max_length=20)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero



class Clientes(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    endereco = models.CharField(max_length=90, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, blank=True, null=True, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento, blank=True)
    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao +' - '+ self.numero

