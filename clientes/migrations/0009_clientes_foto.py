# Generated by Django 3.0 on 2019-12-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20191217_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]