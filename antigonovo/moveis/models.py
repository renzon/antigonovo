from django.db import models


class Movel(models.Model):
    titulo = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    descricao = models.TextField()
    foto = models.ImageField(max_length=200, upload_to='moveis/', null=True)

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'Movel(titulo={self.titulo!r}, preco={self.preco!r}, descricao={self.descricao!r}'
