# Generated by Django 3.0 on 2019-12-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='nome',
            field=models.CharField(max_length=70),
        ),
    ]
