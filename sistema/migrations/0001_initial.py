# Generated by Django 5.1.7 on 2025-03-31 18:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_cadastro', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ano', models.DateField(default=django.utils.timezone.now)),
                ('estudio', models.CharField(max_length=50)),
                ('sinopse', models.TextField()),
                ('data_cadastro', models.DateField(default=django.utils.timezone.now)),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.genero')),
            ],
        ),
    ]
