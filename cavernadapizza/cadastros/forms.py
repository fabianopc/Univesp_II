from django import forms
#from django.contrib.auth.models import User
from .models import Pizza
from .models import Cliente, Endereco

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco']
        
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['endereco',
                  'numero',
                  'complemento',
                  'bairro',
                  'cidade',
                  'estado',
                  'cep']

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['nome', 'valor_p', 'valor_m', 'valor_g', 'descricao', 'imagem']
        widgets = {
            'imagem': forms.FileInput(attrs={'accept': 'image/*'}),

        }
