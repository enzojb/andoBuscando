# Generated by Django 5.1.1 on 2024-10-01 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Propiedad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_propiedad', models.CharField(max_length=100)),
            ],
        ),
    ]