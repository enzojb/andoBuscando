# Generated by Django 5.1.3 on 2024-11-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='direccion',
            field=models.CharField(max_length=55),
        ),
    ]