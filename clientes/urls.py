from django.urls import path
from .views import lista_cliente, novo_cliente, update_cliente, delete_cliente, cliente, busca_cliente

urlpatterns = [
    path('<int:id>', cliente, name='cliente'),
    path('list/', lista_cliente, name='lista_cliente'),
    path('new/', novo_cliente, name='novo_cliente'),
    path('update/<int:id>/', update_cliente, name='update_cliente'),
    path('delete/<int:id>/', delete_cliente, name='delete_cliente'),
    path('busca/', busca_cliente, name='busca_cliente'),
]
