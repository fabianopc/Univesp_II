#from django.shortcuts import render
#from django.forms.models import BaseModelForm
#from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente, Endereco, Pizza
from .forms import ClienteForm, PizzaForm, EnderecoForm 
#from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


###################### CREATE ########################### 
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cadastros/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
        
    def form_valid(self, form):
        user = None
        if 'username' in form.cleaned_data and 'password' in form.cleaned_data:
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            
        cliente = form.save(commit=False)
        cliente.user = user
        cliente.save()
        
        return super().form_valid(form)    
    
class EnderecoCreateView(CreateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'cadastros/endereco_form.html'
    success_url = reverse_lazy('cliente_create') 

class PizzaCreateView(CreateView):
    model = Pizza
    form_class = PizzaForm
    template_name = 'cadastros/pizza_form.html'

    def get_success_url(self):
        return reverse_lazy('pizza_list')

###################### UPDATE ###########################
class ClienteUpdateView(UpdateView):
    model = Cliente
    #form_class = ClienteEnderecoForm
    template_name = 'cadastros/cliente_endereco_form.html'
    success_url = reverse_lazy('cliente_list')

class PizzaUpdateView(UpdateView):
    model = Pizza
    form_class = PizzaForm
    template_name = 'cadastros/pizza_form.html'
#    sucess_url = reverse_lazy('pizza_list')
    def get_success_url(self):
        return reverse_lazy('pizza_list')

###################### LISTAR ##########################
class ClienteListView(ListView):
    model = Cliente
    template_name = 'listas/cliente_list.html'
    context_object_name = 'clientes'

class EnderecoListView(ListView):
    model = Endereco    
    template_name = 'listas/endereco_list.html'

class PizzaListView(ListView):
    model = Pizza
    template_name = 'listas/pizza_list.html'

###################### DELETE ###########################
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cadastros/cliente_delete.html'
    success_url = reverse_lazy('cliente_list')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Exclua o usuário associado ao cliente
        user = self.object.user
        user.delete()
        
        # Em seguida, exclua o endereço associado ao cliente
        endereco = self.object.endereco
        endereco.delete()

        # Finalmente, exclua o cliente
        return super().delete(request, *args, **kwargs)    
    
class PizzaDeleteView(DeleteView):
    model = Pizza
    template_name = 'cadastros/pizza_delete.html'
    success_url = reverse_lazy('pizza_list')
