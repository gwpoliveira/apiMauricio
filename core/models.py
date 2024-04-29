from django.db import models

class Autor(models.Model):
    nome = models.CharField(verbose_name='Nome:', max_length=200)
    def __str__(self):
        return self.nome

# Create your models here.
class livro(models.Model):
    titulo = models.CharField(max_length=200)
    date_pub = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo