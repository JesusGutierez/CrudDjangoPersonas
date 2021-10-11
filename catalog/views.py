from django.shortcuts import render,redirect
from .models import Persona
from .forms import PersonaForm

#Listado de las persona
def inicio(request):
    personas=Persona.objects.all()# select * from persona
    contexto={# creando un diccionario con todos los registros de la entidad Persona
        'personas':personas
    }
    return render(request,'index.html',contexto) #render retorna un objeto httpresponse(index.html)
# Creación de nuevas personas
def crearPersona(request):
    if request.method=='GET':
        form=PersonaForm()
        contexto={
            'form':form
        }
    else:
        form=PersonaForm(request.POST)
        contexto={
            'form':form
        }
        #print(form)#Prueba para ver el envio de datos en la terminal
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto)

# Editar un registro de Personas
def editarPersona(request,id):
    persona=Persona.objects.get(id=id) # usando get para obtener el registro a editar
    if request.method=='GET':
        form=PersonaForm(instance=persona)
        contexto={
            'form':form
        }
    else:
        form=PersonaForm(request.POST,instance=persona)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'crear_persona.html',contexto)

# Eliminar un registro
def eliminarPersona(request,id):
    persona=Persona.objects.get(id=id)
    persona.delete()
    return redirect('index')