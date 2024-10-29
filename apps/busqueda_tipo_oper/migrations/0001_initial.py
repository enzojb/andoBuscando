# Generated by Django 5.1.1 on 2024-10-29 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('busqueda', '0001_initial'),
        ('tipo_operacion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusquedaTipoOper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busqueda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.busqueda')),
                ('tipo_operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_operacion.tipooperacion')),
            ],
        ),
    ]
