from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    titulo = 'TeamBuilder'
    prueba = 5+4+3+2+1
    ctx = {'titulo':titulo, 'loca':prueba}
    return render_to_response('main/index.html', ctx, context_instance=RequestContext(request))

def contact(request):
    titulo = 'Pagina Contacto'
    ctx = {'titulo':titulo}
    return render_to_response('main/contact.html', ctx, context_instance=RequestContext(request))