from django.utils import timezone
from django.db import models

# Aqui vai ficar a classe modelo do Usuário
# nome, sobrenome, cpf, telefone, email, foto, endereço.
# data_cadastro, ativo
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11) # max_length -> numero de caracter
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True) 

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Filme(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.DateField(default=timezone.now)
    estudio = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopse = models.TextField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome #toda vez que vc mensionar o objeto, ele vai mostrar o objeto por exemplo "carros 2" inves de "Filme Object (1)" para isso que serve

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome