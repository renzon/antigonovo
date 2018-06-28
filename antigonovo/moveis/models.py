from django.db import models


class Movel(models.Model):
    titulo = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    descricao = models.TextField()
