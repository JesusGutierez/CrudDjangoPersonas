from django.contrib import admin
from .models import Persona # Importando la clase persona de models
admin.site.register(Persona) # Hacer visible el modelo en el sitio web
# Register your models here.
