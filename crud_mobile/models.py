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
    
class Especie(models.Model):
    idespecie = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'especie'

    def __str__(self):
        return self.descricao

class Raca(models.Model):
    idraca = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'raca'

    def __str__(self):
        return self.descricao
    
class Pet(models.Model):
    idpet = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    idade = models.IntegerField()
    especie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='especie')
    raca = models.ForeignKey(Raca, models.DO_NOTHING, db_column='raca')

    class Meta:
        managed = False
        db_table = 'pet'

    def __str__(self):
        return self.nome