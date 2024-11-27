# from django.shortcuts import render <-- esta libreria no la usamos por ahora
from rest_framework import viewsets, mixins
from .serializer import ProgrammerSerializer
from .models import programmer

from django_filters.rest_framework import DjangoFilterBackend  # libreria de filtros

# Create your views here.


class ProgrammerViewSet(viewsets.ModelViewSet):
    # acá creamos una consulta o QUERY a nuestra tabla, trayendo todos los campos como un objeto.
    queryset = programmer.objects.all()
    # Agregamos la clase ProgrammerSerializer que ya tiene el modelo serializado para mostrar
    serializer_class = ProgrammerSerializer
    # Configuramos el backend de filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['language', 'age', 'is_active']  # Campos filtrables

# class ExperienceViewSet(mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         viewsets.GenericViewSet):
