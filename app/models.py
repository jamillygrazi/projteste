from django.db import models

# Create your models here.

class Person(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    senha = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    endereço = models.TextField()
    cpf = models.CharField(max_length=14)
    def __str__(self):
        return self.cpf + ' - ' + self.nome