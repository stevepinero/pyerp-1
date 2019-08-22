# Generated by Django 2.2.4 on 2019-08-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_pyaccountmove'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyAccountMoveLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('move', models.ForeignKey(on_delete='cascade', related_name='lines', to='account.PyAccountMove')),
            ],
        ),
    ]