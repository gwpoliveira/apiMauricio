from django.shortcuts import render

from .models import Autor, livro
from rest_framework import viewsets
from .serializers import AutorSerializer, livroSerializer


def home(request):
    autores = Autor.objects.all()
    return render(request, 'home.html', context={'autores': autores})


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


# Create your views here.
