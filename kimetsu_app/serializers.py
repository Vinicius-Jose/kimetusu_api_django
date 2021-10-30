from kimetsu_app.models import Grupo, Personagem, Raca
from rest_framework import serializers


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['pk', 'nome', 'descricao']


class RacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = ['pk', 'nome', 'descricao']


class PersonagemSerializer(serializers.ModelSerializer):
    grupo = serializers.PrimaryKeyRelatedField(read_only=False,
                                               queryset=Grupo.objects.all())
    raca = serializers.PrimaryKeyRelatedField(read_only=False,
                                              queryset=Raca.objects.all())

    class Meta:
        model = Personagem
        fields = ['pk', 'nome', 'grupo', 'raca',
                  'apelidos', 'genero', 'idade',
                  'episodio_estreia', 'altura',
                  'peso', 'imagem']
