from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def saluda (request):
    return HttpResponse ('<h1>Hola a todos!<h1> :)')
  
def segundaView(request):
    return  HttpResponse ("""
                          <h1> bienvenidos a mi web </h1>
                    """      )
    
def diaHoy(request):
    dia = datetime.now()
    documento = f'Hoy es: {dia}'
    return HttpResponse (documento)

def SaludaConNombre(request, nombre):
    documento = f'Mi nombre es {nombre}'
    return HttpResponse (documento)
    saludaNombre (name='ailen')
    
def pages (request):
    miHtml= open(r"C:\Users\Sascha\Desktop\AilenPaez\sistema\sistema\templates\templates.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContext = Context({
        'miNombre': 'Ailen',
        'notas':[8,5,4,10]
    })
    documento = plantilla.render(miContext)
    return HttpResponse (documento)

