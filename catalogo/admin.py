from django.contrib import admin
from .models import Filme, Diretor, Categoria

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "diretor", "categoria")
    search_fields = ("titulo",)
    list_filter = ("diretor", "categoria", "ano")

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
