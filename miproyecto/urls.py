"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from miproyecto.miproyecto.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib import admin
from django.urls import path
from catalog.views import inicio,crearPersona,editarPersona,eliminarPersona
from catalog.class_view import PersonaList,PersonaCreate,PersonaUpdate,PersonaDelete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',inicio,name='index'),
    path('',PersonaList.as_view(),name='index'),
    #path('crear_persona/',crearPersona,name='crear_persona'),
    path('crear_persona/',PersonaCreate.as_view(),name='crear_persona'),
    #path('editar_persona/<int:id>/',editarPersona,name='editar_persona'),#ruta con el id
    path('editar_persona/<int:pk>/',PersonaUpdate.as_view(),name='editar_persona'),
    #path('eliminar_persona/<int:id>/',eliminarPersona,name='eliminar_persona')
    path('eliminar_persona/<int:pk>/',PersonaDelete.as_view(),name='eliminar_persona')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)