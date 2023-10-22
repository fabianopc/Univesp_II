#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente, Endereco, Pizza
from .forms import ClienteEnderecoForm, PizzaForm 
#from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.


###################### CREATE ########################### 
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteEnderecoForm
    template_name = 'cadastros/cliente_endereco_form.html'
    success_url = reverse_lazy('cliente_list')
    
    def form_valid(self, form):
        # Extraia os dados do formulário
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        endereco_data = {
            'endereco': form.cleaned_data['endereco'],
            'numero': form.cleaned_data['numero'],
            'complemento': form.cleaned_data['complemento'],
            'bairro': form.cleaned_data['bairro'],
            'cidade': form.cleaned_data['cidade'],
            'estado': form.cleaned_data['estado'],
            'cep': form.cleaned_data['cep']
        }
        
    # Crie um novo usuário se as credenciais forem fornecidas
        if username and password:
            user = User.objects.create_user(username=username, password=password)
        else:
            # Se as credenciais não forem fornecidas, defina user como None
            user = None

        # Crie o cliente
        cliente = form.save(commit=False)
        cliente.user = user
        cliente.save()

        # Crie o endereço associado ao cliente
        endereco = Endereco.objects.create(cliente=cliente, **endereco_data)

        return super().form_valid(form)
    

class PizzaCreateView(CreateView):
    model = Pizza
    form_class = PizzaForm
    template_name = 'cadastros/pizza_form.html'

    def get_success_url(self):
        return reverse_lazy('pizza_list')

###################### UPDATE ###########################
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteEnderecoForm
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
    
class PizzaDeleteView(DeleteView):
    model = Pizza
    template_name = 'cadastros/pizza_delete.html'
    success_url = reverse_lazy('pizza_list')
