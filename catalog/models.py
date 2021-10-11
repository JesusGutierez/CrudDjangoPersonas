from django.db import models
class Persona(models.Model): # models.Model permite heredar todo lo que tiene la libreria models
    id=models.AutoField(primary_key=True) # campo clave auto incrementable
    nombre=models.CharField(max_length=100) # campo tipo caracter
    apellido=models.CharField(max_length=120) # campo tipo caracter
    correo=models.CharField(max_length=200) # campo tipo caracter
    imagen=models.ImageField(upload_to="fotos",null=True)
    def __str__(self):
        return self.nombre
# Create your models here.
