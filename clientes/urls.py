from django.urls import path
from .views import lista_cliente, novo_cliente, update_cliente
from .views import delete_cliente, cliente, busca_cliente
from .views import ClienteDetail, ClienteList, ClienteCreate
from .views import ClienteUpdate, ClienteDelete

urlpatterns = [
    path('<int:id>/', cliente, name='cliente'),
    path('list/', lista_cliente, name='lista_cliente'),
    path('new/', novo_cliente, name='novo_cliente'),
    path('update/<int:id>/', update_cliente, name='update_cliente'),
    path('delete/<int:id>/', delete_cliente, name='delete_cliente'),
    path('busca/', busca_cliente, name='busca_cliente'),
    path('cliente_list/', ClienteList.as_view(), name='cliente_list'),
    path('cliente_detail/<int:pk>/', ClienteDetail.as_view(), name='cliente_detail'),
    path('cliente_form/', ClienteCreate.as_view(), name='cliente_form'),
    path('cliente_update/<int:pk>/', ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente_delete/<int:pk>/', ClienteDelete.as_view(), name='cliente_delete')
]
