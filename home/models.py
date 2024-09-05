from django.db import models

# Create your models here.

class Estoque(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    marca = models.CharField(max_length=70)
    produto = models.CharField(max_length=70)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    