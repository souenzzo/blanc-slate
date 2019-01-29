from django.db import models

# Create your models here.

class Sala(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Horario(models.Model):
    dia_da_semana = models.CharField(max_length=50)
    horario = models.TimeField()
    def __str__(self):
        return self.dia_da_semana + ' ' + self.horario.strftime("%H:%M")

class Modalidade(models.Model):
    nome = models.CharField(max_length=200)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Aluna(models.Model):
    nome = models.CharField(max_length=200)
    disponivel_em = models.ManyToManyField(Horario) ## precisa de through?
    pratica = models.ManyToManyField(Modalidade)  ## precisa de through?
    def __str__(self):
        return self.nome

class Professora(models.Model):
    nome = models.CharField(max_length=200)
    disponivel_em = models.ManyToManyField(Horario)
    ensina = models.ManyToManyField(Modalidade)
    def __str__(self):
        return self.nome

