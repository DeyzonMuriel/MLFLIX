from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    ano = models.PositiveIntegerField()
    sinopse = models.TextField(blank=True)
    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, related_name="filmes")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="filmes")

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
