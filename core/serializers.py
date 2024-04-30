from .models import Autor, livro
from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class livroSerializer(serializers.ModelSerializer):
        class Meta:
            model = livro
            fields = '__all__'
