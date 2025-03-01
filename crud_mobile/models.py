from django.db import models

# Create your models here.
class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nome