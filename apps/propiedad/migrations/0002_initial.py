# Generated by Django 5.1.3 on 2024-11-12 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propiedad', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='agente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.agente'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.localidad'),
        ),
        migrations.AddField(
            model_name='propiedadfoto',
            name='propiedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.propiedad'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tipo_propiedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedad.tipopropiedad'),
        ),
    ]