from django.urls import path
from .views import lista_cliente, novo_cliente, update_cliente, delete_cliente, pessoa

urlpatterns = [
    path('<int:id>', pessoa, name='pessoa'),
    path('list/', lista_cliente, name='lista_cliente'),
    path('new/', novo_cliente, name='novo_cliente'),
    path('update/<int:id>/', update_cliente, name='update_cliente'),
    path('delete/<int:id>/', delete_cliente, name='delete_cliente'),
]