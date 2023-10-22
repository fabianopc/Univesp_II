from django.shortcuts import render
from cadastros.models import Pizza
from django.views.generic import TemplateView



# Create your views here.
#class PaginaView(TemplateView):
#    template_name = 'paginas/index.html'
def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'paginas/index.html', {'pizzas': pizzas})

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
