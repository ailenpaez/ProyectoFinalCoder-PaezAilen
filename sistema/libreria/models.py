from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entrenamiento(models.Model):
    nombre= models.CharField(max_length=50)
    nivel= models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} | Nivel: {self.nivel}'
    
class Deportista(models.Model):
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField((""), max_length=254)
    
    def __str__(self):
        return f'{self.nombre}{self.apellido}'
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField((""), max_length=254)
    deporte = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Asistencia(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_comienzo = models.DateField()
    asistio = models.BooleanField()
    
    
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    


    