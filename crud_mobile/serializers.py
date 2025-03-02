from rest_framework import serializers
from .models import Usuario, Pet

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idusuario', 'nome', 'idade', 'email']  # Inclua todos os campos necessários

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['idpet', 'nome', 'idade', 'especie', 'raca']  # Inclua todos os campos necessários