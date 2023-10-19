from django.urls import path
from .views import ClienteEnderecoCreateView, ClienteEnderecoDeleteView, EnderecoListView, ClienteListView, ClienteEnderecoUpdateView
from .views import PizzaListView, PizzaCreateView, PizzaUpdateView, PizzaDeleteView


urlpatterns = [
    path('cliente/create', ClienteEnderecoCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/delete', ClienteEnderecoDeleteView.as_view(), name='cliente_delete'),
    path('cliente/<int:pk>/update', ClienteEnderecoUpdateView.as_view(), name='cliente_update'),
    path('cliente/list', ClienteListView.as_view(), name='cliente_list'),
    path('endereco/list', EnderecoListView.as_view(), name='endereco_list'),

    path('pizza/list', PizzaListView.as_view(), name='pizza_list'),
    path('pizza/create', PizzaCreateView.as_view(), name='pizza_create'),
    path('pizza/<int:pk>/update', PizzaUpdateView.as_view(), name='pizza_update'),
    path('pizza/<int:pk>/delete', PizzaDeleteView.as_view(), name='pizza_delete'),
]


