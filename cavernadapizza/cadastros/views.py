from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente, Endereco, Pizza, Pedido, ItensPedido
from .forms import ClienteForm, PizzaForm, EnderecoForm, ClienteEnderecoUpdateForm, PedidoForm, ItensPedidoForm 
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
    
class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'cadastros/pedido_form.html'
    success_url = reverse_lazy('pedido_list')
    
    def form_valid(self, form):
        form.instance.cliente = self.request.user.cliente
        return super().form_valid(form)
    
class ItensPedidoCreateView(CreateView):
    model = ItensPedido
    form_class = ItensPedidoForm
    template_name = 'cadastros/itenspedido_form.html'
    success_url = reverse_lazy('pedido_list')
    
    def form_valid(self, form):
        form.instance.pedido = Pedido.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

###################### UPDATE ###########################
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteEnderecoUpdateForm
    template_name = 'cadastros/cliente_update_form.html'
    success_url = reverse_lazy('cliente_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.object  # Obtém a instância do Cliente atual

        # Preencha os campos do formulário com os dados do Cliente, Endereço e Usuário
        context['form'].initial.update({
            'nome': cliente.nome,
            'email': cliente.email,
            'telefone': cliente.telefone,
            'endereco': cliente.endereco.endereco,
            'numero': cliente.endereco.numero,
            'complemento': cliente.endereco.complemento,
            'bairro': cliente.endereco.bairro,
            'cidade': cliente.endereco.cidade,
            'estado': cliente.endereco.estado,
            'cep': cliente.endereco.cep,
            'username': cliente.user.username,
            'password': ''  # A senha não é preenchida por razões de segurança
        })

        context['form'].fields['password'].required = False

        return context
    
    def form_valid(self, form):
        # Obtenha a instância do cliente atual
        cliente = form.save(commit=False)

        # Atualize as informações do cliente com os dados do formulário
        cliente.nome = form.cleaned_data['nome']
        cliente.email = form.cleaned_data['email']
        cliente.telefone = form.cleaned_data['telefone']
                
        # Obtenha a instância do endereço associado ao cliente
        endereco = cliente.endereco
        endereco.endereco = form.cleaned_data['endereco']
        endereco.numero = form.cleaned_data['numero']
        endereco.complemento = form.cleaned_data['complemento']
        endereco.bairro = form.cleaned_data['bairro']
        endereco.cidade = form.cleaned_data['cidade']
        endereco.estado = form.cleaned_data['estado']
        endereco.cep = form.cleaned_data['cep']
        
        user = cliente.user
        user.username = form.cleaned_data['username']
        
        # Se uma nova senha for fornecida, atualize-a
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
            
        # Salve as alterações
        endereco.save()
        user.save()
        cliente.save()
        
        messages.success(self.request, 'Dados atualizados com sucesso')
        return redirect(self.get_success_url())

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
    
class PedidoListView(ListView):
    model = Pedido
    template_name = 'listas/pedido_list.html'
    context_object_name = 'pedidos'

###################### DELETE ###########################
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cadastros/cliente_delete.html'
    #success_url = reverse_lazy('cliente_list')
    
    def get(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
            return render(request, self.template_name, {'cliente': cliente})
        except Cliente.DoesNotExist:
            raise Http404("Cliente não encontrado")
    
    def post(self, request ,pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
            cliente.endereco.delete()
            cliente.user.delete()
            cliente.delete()
            return redirect(reverse_lazy('cliente_list'))
        except Cliente.DoesNotExist:
            raise Http404("Cliente não encontrado")               
    
class PizzaDeleteView(DeleteView):
    model = Pizza
    template_name = 'cadastros/pizza_delete.html'
    success_url = reverse_lazy('pizza_list')
