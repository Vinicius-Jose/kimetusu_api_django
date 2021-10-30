from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy

# Create your models here.


class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)


class Raca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)


class Genero(models.TextChoices):
    MASCULINO = 'M', gettext_lazy('Masculino')
    FEMININO = 'F', gettext_lazy('Feminino')


class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo,
                              related_name='grupo', on_delete=CASCADE)
    raca = models.ForeignKey(Raca,
                             related_name='raca', on_delete=CASCADE)
    apelidos = models.CharField(max_length=500)
    genero = models.CharField(max_length=1, choices=Genero.choices,
                              default=Genero.MASCULINO)
    idade = models.IntegerField()
    episodio_estreia = models.IntegerField()
    altura = models.FloatField(help_text='Altura em Metros')
    peso = models.FloatField(help_text='Peso em kilos')
    imagem = models.ImageField(help_text='Imagem do personagem',
                               max_length=600, upload_to='./photos')
