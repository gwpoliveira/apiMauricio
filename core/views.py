from django.shortcuts import render
from .models import Autor, livro

def home(request):
    autores = Autor.objects.all()
    return render(request, 'home.html', context={'autores':autores})

# Create your views here.
