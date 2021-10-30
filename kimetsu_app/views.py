from django.shortcuts import render
from rest_framework import viewsets
from .models import Grupo, Raca, Personagem
from .serializers import (GrupoSerializer,
                          RacaSerializer,
                          PersonagemSerializer)

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class GrupoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Grupo to be viewed or edited.
    """
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome']
    filterset_fields = ['nome']


class RacaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Raca to be viewed or edited.
    """
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome']
    filterset_fields = ['nome']


class PersonagemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Personagem to be viewed or edited.
    """
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome', 'apelidos']
    filterset_fields = ['nome', 'raca', 'apelidos',
                        'genero', 'idade', 'episodio_estreia',
                        'altura', 'peso']
