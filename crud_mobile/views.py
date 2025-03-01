from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.db import connection

@api_view(['POST'])
def crud_mobile(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            idade = serializer.validated_data['idade']
            email = serializer.validated_data['email']
            
            # Usando a procedure do banco de dados
            with connection.cursor() as cursor:
                cursor.execute('CALL setusuario(null, %s::varchar, %s::int, %s::varchar)', [nome, idade, email])
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)