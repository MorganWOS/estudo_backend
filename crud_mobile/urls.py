from django.urls import path
from . import views

app_name = 'crud_mobile'

urlpatterns = [
    path('apiusuario/', views.crud_mobile, name='crud_mobile'),  # Rota para a página inicial
    path('apipet/', views.apipet, name='apipet'),
]