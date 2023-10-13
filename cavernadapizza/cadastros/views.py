#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente, Endereco
from .forms import ClienteEnderecoForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

###################### CREATE ########################### 
class ClienteEnderecoCreateView(CreateView):
        
    form_class = ClienteEnderecoForm
    template_name = 'cadastros/cliente_endereco_form.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password'] #Acessa a senha do formulário
        
        # Crie um novo usuário e faça login automaticamente
        user = User.objects.create_user(username=username, password=password)
        user = authenticate(username=username, password=password)
        login(self.request, user)

        #Cliente associado ao usuário
        cliente = form.save(commit=False)
        cliente.user = user
        cliente.save()

        #Endereço associado ao usuário
        endereco = Endereco(
                cliente=cliente,
                endereco=form.cleaned_data['endereco'],
                numero=form.cleaned_data['numero'],
                complemento=form.cleaned_data['complemento'],
                bairro=form.cleaned_data['bairro'],
                cidade=form.cleaned_data['cidade'],
                estado=form.cleaned_data['estado'],
                cep=form.cleaned_data['cep']
        )
        endereco.save()
        return super().form_valid(form)
    success_url = reverse_lazy('cliente_list')
###################### UPDATE ###########################
class ClienteEnderecoUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteEnderecoForm
    template_name = 'cadastros/cliente_endereco_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.object
        #Carrega as informacoes do Endereço associado ao cliente
        endereco = Endereco.objects.get(cliente=cliente)
        #Carrega as informacoes do usuario associado ao cliente
        user = User.objects.get(cliente=cliente)
        context['form'].initial.update({
            'endereco': endereco.endereco,
            'numero': endereco.numero,
            'complemento': endereco.complemento,
            'bairro': endereco.bairro,
            'cidade': endereco.cidade,
            'estado': endereco.estado,
            'cep': endereco.cep,
            'username': user.username,
            'password': user.password,  # Isso exibirá a senha no campo (não recomendado em produção)
        })
        return context

    def fom_valid(self, form):
        # Atualizar o cliente com as informações do formulário
        cliente = form.save()

        # Atualizar as informações do endereço associado ao cliente
        endereco = Endereco.objects.get(cliente=cliente)
        endereco.endereco = form.cleaned_data['endereco']
        endereco.numero = form.cleaned_data['numero']
        endereco.complemento = form.cleaned_data['complemento']
        endereco.bairro = form.cleaned_data['bairro']
        endereco.cidade = form.cleaned_data['cidade']
        endereco.estado = form.cleaned_data['estado']
        endereco.cep = form.cleaned_data['cep']
        endereco.save()

        # Atualizar as informações do usuário associado ao cliente
        user = User.objects.get(cliente=cliente)
        user.username = form.cleaned_data['username']
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
    sucess_url = reverse_lazy('cliente_list')


###################### LISTAR ##########################
class ClienteListView(ListView):
    model = Cliente
    template_name = 'listas/cliente_list.html'

class EnderecoListView(ListView):
    model = Endereco    
    template_name = 'listas/endereco_list.html'


###################### DELETE ###########################
class ClienteEnderecoDeleteView(DeleteView):
    model = Cliente
    template_name = 'cadastros/cliente_delete.html'
    success_url = reverse_lazy('cliente_list')


