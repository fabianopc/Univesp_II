from django.urls import path
from . import views

#Importa view que foi criada
from .views import SobreView

urlpatterns = [
#    path('', PaginaView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]
