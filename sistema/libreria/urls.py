from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from sistema.views import saluda, segundaView, diaHoy, SaludaConNombre, pages
from libreria.views import *

urlpatterns = [
    path('nuevo-entrenamiento/<nombre>/<nivel>', entrenamiento),
    path('', inicio, name= 'Inicio'),
    #path('lista-sports/',listaSports),
    path('sports/', clases, name='Sports'),
    path('profesores/', profesores, name='Profesores'),
    path('deportistas/', deportistas, name= 'Deportistas'),
    path('asistencias/', asistencias, name= 'Asistencias'), 
    path('pages/', nosotros, name='Nosotros'),  
    path('contacto/', contacto, name='Contacto'),
    path('busqueda-nivel/', busquedaNivel, name='BusquedaNivel'), 
    path('search/', search, name='Search'),
    path('lista-profes/', listaProfesores, name='ListaProfesores'),
    path('nuevo-profe/', nuevoProfe, name='nuevoProfe'), 
    path('delete-profe/<int:id>/', eliminarProfesor, name='eliminarProfesor'),
    path('edit-profe/<int:id>/', editarProfesor, name='editarProfesor'),
    path('lista-sports/', sportsList.as_view() , name='listaSports'),
    path('sports-detail/<pk>', sportsDetail.as_view() , name='SportsDetail'),
    path('sports-create/', sportsCreate.as_view() , name='SportsCreate'),
    path('sports-update/<pk>', sportsUpdate.as_view() , name='SportsUpdate'),
    path('sports-delete/<pk>', sportsDelete.as_view() , name='SportsDelete'),
    path('login/', miLogin, name='Login'),
    path('register/', register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editar-perfil/', editar_perfil, name='editPerfil'),
]
