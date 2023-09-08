from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    dni = models.IntegerField()
    telefono = models.CharField(max_length=10)