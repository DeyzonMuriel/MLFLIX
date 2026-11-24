from django.test import TestCase
from django.urls import reverse
from .models import Diretor, Categoria, Filme

class CatalogoTestes(TestCase):
    def setUp(self):
        self.diretor = Diretor.objects.create(nome="Diretor Teste")
        self.categoria = Categoria.objects.create(nome="Drama")
        Filme.objects.create(
            titulo="Filme de Teste", ano=2024,
            diretor=self.diretor, categoria=self.categoria
        )

    def test_pagina_inicial_abre(self):
        resposta = self.client.get(reverse("listar_filmes"))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Filme de Teste")

    def test_pesquisa_por_titulo(self):
        resposta = self.client.get(reverse("listar_filmes"), {"q": "teste"})
        self.assertContains(resposta, "Filme de Teste")

    def test_filtro_por_diretor(self):
        resposta = self.client.get(reverse("listar_filmes"), {"diretor": self.diretor.id})
        self.assertContains(resposta, "Filme de Teste")
