# myapp/models.py
from django.db import models

class Objeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class MeuObjeto(models.Model):
    campo_texto = models.CharField(max_length=100)

    def __str__(self):
        return self.campo_texto