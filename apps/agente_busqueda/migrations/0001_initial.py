# Generated by Django 5.1.1 on 2024-10-29 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agente', '0001_initial'),
        ('busqueda', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgenteBusqueda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agente.agente')),
                ('busqueda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.busqueda')),
            ],
        ),
    ]
