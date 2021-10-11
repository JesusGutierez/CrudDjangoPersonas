from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse_lazy

class PersonaList(ListView):
    model=Persona
    template_name='index.html'
    #def get_queryset(self):# este método nos permite realizar filtros
    #    return self.model.objects.all()[:2]# filtrando Persona solo los 2 últimos registros

class PersonaCreate(CreateView):
    model=Persona
    form_class=PersonaForm
    template_name='crear_persona.html'
    success_url=reverse_lazy('index')#redireccionando al archivo index.html

class PersonaUpdate(UpdateView):
    model=Persona
    form_class=PersonaForm
    template_name='crear_persona.html'
    success_url=reverse_lazy('index')

class PersonaDelete(DeleteView):
    model=Persona
    template_name='verificacion.html'
    success_url=reverse_lazy('index')