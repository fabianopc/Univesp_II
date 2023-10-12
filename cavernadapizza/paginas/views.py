#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PaginaView(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
