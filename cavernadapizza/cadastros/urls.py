from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ClienteCreateView, ClienteUpdateView, ClienteListView, ClienteDeleteView
from .views import EnderecoCreateView, EnderecoListView
from .views import PizzaListView, PizzaCreateView, PizzaUpdateView, PizzaDeleteView


urlpatterns = [
    path('cliente/create', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/delete', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('cliente/<int:pk>/update', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/list', ClienteListView.as_view(), name='cliente_list'),
    
    path('endereco/create', EnderecoCreateView.as_view(), name='endereco_create'),
    path('endereco/list', EnderecoListView.as_view(), name='endereco_list'),    

    path('pizza/list', PizzaListView.as_view(), name='pizza_list'),
    path('pizza/create', PizzaCreateView.as_view(), name='pizza_create'),
    path('pizza/<int:pk>/update', PizzaUpdateView.as_view(), name='pizza_update'),
    path('pizza/<int:pk>/delete', PizzaDeleteView.as_view(), name='pizza_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
