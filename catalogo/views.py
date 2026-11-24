from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Filme, Diretor, Categoria

def listar_filmes(request):
    # Lê os valores enviados pela URL usando GET.
    pesquisa = request.GET.get("q", "").strip()
    diretor_id = request.GET.get("diretor", "")
    categoria_id = request.GET.get("categoria", "")

    # Começa com todos os filmes e aplica os filtros antes da paginação.
    filmes = Filme.objects.select_related("diretor", "categoria").all()

    if pesquisa:
        filmes = filmes.filter(titulo__icontains=pesquisa)

    if diretor_id:
        filmes = filmes.filter(diretor_id=diretor_id)

    if categoria_id:
        filmes = filmes.filter(categoria_id=categoria_id)

    # Divide o resultado filtrado em páginas de cinco filmes.
    paginator = Paginator(filmes, 5)
    numero_pagina = request.GET.get("page")
    pagina = paginator.get_page(numero_pagina)

    # Mantém pesquisa e filtros nos links de próxima/anterior.
    parametros = request.GET.copy()
    parametros.pop("page", None)
    querystring = parametros.urlencode()

    contexto = {
        "pagina": pagina,
        "diretores": Diretor.objects.all(),
        "categorias": Categoria.objects.all(),
        "pesquisa": pesquisa,
        "diretor_selecionado": diretor_id,
        "categoria_selecionada": categoria_id,
        "querystring": querystring,
    }
    return render(request, "catalogo/lista_filmes.html", contexto)
