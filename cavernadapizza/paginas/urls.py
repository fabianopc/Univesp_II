from django.urls import path

#Importa view que foi criada
from .views import PaginaView, SobreView

urlpatterns = [
    path('', PaginaView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]
