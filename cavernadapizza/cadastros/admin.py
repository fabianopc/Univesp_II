from django.contrib import admin

#Importar as classes
from .models import Cliente, Endereco
from .models import Pizza

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Pizza)

