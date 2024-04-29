from django.contrib import admin
from .models import Autor, livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)

@admin.register(livro)
class LivroAdmin(admin.ModelAdmin):
    model = livro
    list_display = ('titulo', 'autor')
    search_fields = ('titulo','autor')
    list_filter = ('autor','autor')
