# Generated by Django 3.0 on 2019-12-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20191212_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='clientes',
            name='departamentos',
            field=models.ManyToManyField(blank=True, null=True, to='clientes.Departamento'),
        ),
    ]
