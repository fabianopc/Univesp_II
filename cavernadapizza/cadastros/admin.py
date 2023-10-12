from django.contrib import admin

#Importar as classes
from .models import Cliente, Endereco

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Endereco)

