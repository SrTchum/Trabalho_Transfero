from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gênero")

    def __str__(self):
        return self.nome

class Filme(models.Model):  # 👈 Nome corrigido
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    estudio = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopse = models.TextField()

    def __str__(self):
        return f"{self.nome} ({self.ano})"