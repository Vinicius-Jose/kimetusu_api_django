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
    imc = serializers.SerializerMethodField('calc_imc')

    def calc_imc(self, obj):
        return obj.peso / (obj.altura**2)

    class Meta:
        model = Personagem
        read_only_fields = ['imc']
        fields = ['pk', 'nome', 'grupo', 'raca',
                  'apelidos', 'genero', 'idade',
                  'episodio_estreia', 'altura',
                  'peso', 'imagem', 'imc']
