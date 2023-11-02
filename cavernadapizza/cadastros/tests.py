from django.test import TestCase
from .models import Endereco, Cliente
from django.contrib.auth.models import User

class EnderecoTest(TestCase):
    def setUp(self):
        # Criando um usuário para usar como chave estrangeira
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.endereco = Endereco.objects.create(
            endereco='Rua Teste',
            numero=123,
            complemento='Apto 101',
            bairro='Bairro Teste',
            cidade='Cidade Teste',
            estado='TS',
            cep='12345-678',
        )

        self.cliente = Cliente.objects.create(
            user=self.user,
            nome='Teste Cliente',
            email='cliente@teste.com',
            telefone='123-456-7890',
            endereco=self.endereco,
        )

    def test_endereco_str(self):
        self.assertEqual(str(self.endereco), 'Rua Teste')

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), 'Teste Cliente')

class ClienteEnderecoRelationTest(TestCase):
    def test_cliente_endereco_relation(self):
        # Criando um usuário
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Criando um endereço
        endereco = Endereco.objects.create(
            endereco='Rua Teste',
            numero=123,
            complemento='Apto 101',
            bairro='Bairro Teste',
            cidade='Cidade Teste',
            estado='TS',
            cep='12345-678',
        )

        # Criando um cliente associado a esse endereço
        cliente = Cliente.objects.create(
            user=user,
            nome='Teste Cliente',
            email='cliente@teste.com',
            telefone='123-456-7890',
            endereco=endereco,
        )

        # Verificando se o cliente está associado ao endereço
        self.assertEqual(cliente.endereco, endereco)
