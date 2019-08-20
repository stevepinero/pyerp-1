# Generated by Django 2.2.4 on 2019-08-18 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyaccountplan',
            name='type',
            field=models.CharField(choices=[('activo', 'Activo'), ('pasivo', 'Pasivo'), ('patrimonio_capital', 'Patrimonio'), ('ingresos', 'Ingresos'), ('costos', 'Costos'), ('gastos', 'Gastos')], default='activo', max_length=64),
        ),
    ]