from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entrenamiento, Profesor, Avatar
from .forms import Contacto, ProfeForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView , UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def entrenamiento(self, nombre, nivel):
    
    entrenamiento = Entrenamiento(nombre=nombre, nivel=nivel)
    entrenamiento.save()
    
    return HttpResponse(f"""
     <p> Entrenamiento: {entrenamiento.nombre} | Nivel: {entrenamiento.nivel} ha sido creado! </p>
                        """)
    
def listaSports (self):
    lista = Entrenamiento.objects.all()
    return render(self, 'lista_entrenamientos.html',{'listaSports': lista})

def inicio(request):
    
    try:
        avatar=Avatar.objects.get(user=request.user.id)
        return render (request,'inicio.html',{'url':avatar.imagen.url})
    except:
        return render (request, 'inicio.html')

def clases(self):
    return render (self, 'sports.html')

def profesores(self):
    return render (self, 'profesores.html')

def deportistas (self):
    return render (self, 'deportistas.html')

def asistencias(self):
    return render (self, 'asistencias.html')

def nosotros(self):
    return render (self, 'nosotros.html')

def contacto (request):
    
    print('method: ', request.method)
    print ('post: ', request.POST)   
    
    if request.method == 'POST': 
        miContacto = Contacto(request.POST)
        
        print(miContacto)
        
        if miContacto.is_valid():
            data = miContacto.cleaned_data
            entrenamiento = Entrenamiento(nombre=data['entrenamiento'], nivel=data['nivel'])
            entrenamiento.save()
    
            return render(request, 'formularioEnviado.html')

        else:
            return render (request,'inicio.html', {'mensaje': 'Formulario inválido.'})
        
    
    else: 
        miContacto = Contacto()
        
        
    return render (request, 'contacto.html', {'miContacto': miContacto})



def busquedaNivel(request):
    return render (request, 'busquedaNivel.html')


def search (request):
    
    if request.GET["nivel"]:
        nivel = request.GET["nivel"]
        entrenamiento = Entrenamiento.objects.filter(nivel=nivel)
        return render (request,'resultadoBusqueda.html',{'entrenamiento':entrenamiento, 'nivel':nivel})
    
    else: 
        return HttpResponse(f'No enviaste información.')
    
@staff_member_required(login_url='/app-sports')
def listaProfesores(request):
    profesores= Profesor.objects.all()
    return render (request, 'listaProfes.html', {'profesores':profesores})

# MI CRUD PARA PROFESORES

def nuevoProfe(request):
    
    print('method: ', request.method)
    print ('post: ', request.POST)   
    
    if request.method == 'POST': 
        miForm = ProfeForm(request.POST)
        
        if miForm.is_valid():
            data = miForm.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], deporte=data['deporte'])
            profesor.save()
            return HttpResponseRedirect('/app-sports/')
        
        else:
            return render (request,'inicio.html', {'mensaje': 'Formulario inválido.'})
    else: 
        miForm = ProfeForm()
        
    return render (request, 'profeform.html', {'miForm': miForm})


#ESTA FUNCION SOLO APLICA PARA LOS PROFES CREADOS EN LA FUNCION DE ARRIBA.
def eliminarProfesor(request, id):
    
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        
        profesores = Profesor.objects.all()
        return render(request, 'listaProfes.html', {'profesores':profesores} )
    
    
#FUNCION PARA EDITAR PROFESORES

def editarProfesor(request, id):
    
    print('method: ', request.method)
    print ('post: ', request.POST)   
    
   
    profesor = Profesor.objects.get(id=id)
        
    if request.method == 'POST': 
        miForm = ProfeForm(request.POST)
            
        if miForm.is_valid():
            data = miForm.cleaned_data
            #profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.deporte = data ['deporte']
            profesor.save()
            
            return HttpResponseRedirect('/app-sports/')
        
        else:
            return render (request,'inicio.html', {'mensaje': 'Formulario inválido.'})
    else: 
        miForm = ProfeForm(initial={
            "nombre" : profesor.nombre , 
            "apellido" : profesor.apellido , 
            "email" : profesor.email,
            "deporte" : profesor.deporte ,
            })
        
    return render (request, 'editarForm.html', {'miForm': miForm, 'id': profesor.id})


# FIN DEL CRUD PROFESORES.

# CRUD PARA DEPORTES - VISTAS BASADAS EN CLASES. (read)

class sportsList(LoginRequiredMixin, ListView):
    
    model = Entrenamiento
    template_name = 'sportsList.html'
    context_object_name = 'sports'
    
    
class sportsDetail(DetailView):
    
    model = Entrenamiento
    template_name = 'sportDetail.html'
    context_object_name = 'sport'
    
class sportsCreate(CreateView):
    
    model = Entrenamiento
    template_name = 'sportCreate.html'
    fields = ['nombre', 'nivel']
    success_url = '/app-sports/'
    
class sportsUpdate (UpdateView):
    model = Entrenamiento
    template_name = 'sportUpdate.html'
    fields = ('__all__')
    success_url = '/app-sports/'
    context_object_name = 'sport'
    
class sportsDelete (DeleteView):
     model = Entrenamiento
     template_name = 'sportDelete.html'
     success_url = '/app-sports/'
     
#FIN DEL CRUD DEPORTES.

#FUNCIÓN PARA EL LOGIN.

def miLogin (request):

    if request.method == 'POST': 
        miForm = AuthenticationForm(request, data=request.POST)
        
        if miForm.is_valid():
            data = miForm.cleaned_data
            usuario = data["username"]
            pwd = data["password"]
            
            user = authenticate(username=usuario, password=pwd)
            
            if user:
                login(request, user)
                return render( request, 'inicio.html', {"mensaje": f' Hola {usuario}'})
            
            else:
                return render( request, 'inicio.html', {"mensaje": f' ERROR| Los datos ingresados son incorrectos.'})
        
        else:
            return render (request,'inicio.html', {"mensaje": 'Formulario inválido.'})
    else: 
        miForm = AuthenticationForm()
        
    return render (request, 'login.html', {"miForm": miForm})

#FUNCIÓN DE REGISTRO

def register(request):
    
    if request.method == 'POST': 
        miForm = UserCreationForm(request.POST)
        
        if miForm.is_valid():
            data = miForm.cleaned_data
            username = data["username"]
            miForm.save()
            return render(request, 'inicio.html', {"mensaje": f'El usuario {username} ha sido creado!' })
        else:
            return render (request,'inicio.html', {"mensaje": 'Formulario inválido.'})
    else: 
        miForm = UserCreationForm()
        
    return render (request, 'registro.html', {"miForm": miForm})


@login_required
def editar_perfil(request):
    usuario = request.user        
    if request.method == 'POST': 
        miForm = UserEditForm(request.POST, instance=request.user)
            
        if miForm.is_valid():
            data = miForm.cleaned_data
            usuario.email = data['email']
            usuario.nombre = data['first_name']
            usuario.apellido = data['last_name']
            usuario.set_passwoed=data['password1']
            usuario.save()
            
            return render (request,'inicio.html', {'mensaje': 'Datos Actualizados'})
        
        else:
            return render (request,'inicio.html', {'mensaje': 'Formulario inválido.'})
    else: 
        miForm = UserEditForm(instance=request.user)
        return render (request, 'editarPerfil.html', {'miForm': miForm})
    
    
def my_view(request):
    return render(request, 'asistencias.html')

def volverInicio(request):
    return render(request, 'inicio.html')