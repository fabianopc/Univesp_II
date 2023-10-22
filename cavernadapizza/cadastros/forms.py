from django import forms
from django.contrib.auth.models import User
from .models import Pizza
from .models import Cliente, Endereco

class ClienteEnderecoForm(forms.ModelForm):
    # Campos do modelo Cliente
    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    # Campos do modelo Endereco
    endereco = forms.CharField(max_length=200)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length=100, required=False)
    bairro = forms.CharField(max_length=100)
    cidade = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=2)
    cep = forms.CharField(max_length=10)

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'username', 'password', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']

    def save(self, commit=True):
        # Verifique se o usuário informou um nome de usuário e senha
        if 'username' in self.cleaned_data and 'password' in self.cleaned_data:
            # Crie um novo usuário
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password']
            )
        else:
            # Se o usuário não informou nome de usuário e senha, obtenha o usuário existente
            user = User.objects.get(username=self.cleaned_data['username'])

        # Crie ou atualize o cliente
        cliente, created = Cliente.objects.get_or_create(
            user=user,
            defaults={
                'nome': self.cleaned_data['nome'],
                'email': self.cleaned_data['email'],
                'telefone': self.cleaned_data['telefone'],
            }
        )

        # Crie ou atualize o endereço associado ao cliente
        endereco, created = Endereco.objects.get_or_create(
            cliente=cliente,
            defaults={
                'endereco': self.cleaned_data['endereco'],
                'numero': self.cleaned_data['numero'],
                'complemento': self.cleaned_data['complemento'],
                'bairro': self.cleaned_data['bairro'],
                'cidade': self.cleaned_data['cidade'],
                'estado': self.cleaned_data['estado'],
                'cep': self.cleaned_data['cep']
            }
        )

        return cliente

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['nome', 'valor_p', 'valor_m', 'valor_g', 'descricao', 'imagem']
        widgets = {
            'imagem': forms.FileInput(attrs={'accept': 'image/*'}),

        }
