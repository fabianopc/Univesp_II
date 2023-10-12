from django import forms
from django.contrib.auth.models import User
from .models import Cliente, Endereco

class ClienteEnderecoForm(forms.ModelForm):
    # Campos do modelo Cliente
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=20)

    # Campos do modelo Endereco
    endereco = forms.CharField(max_length=200)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length=100, required=False)
    bairro = forms.CharField(max_length=100)
    cidade = forms.CharField(max_length=100)
    estado = forms.CharField(max_length=2)
    cep = forms.CharField(max_length=10)

    # Campos para o usuário (nome de usuário e senha)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

