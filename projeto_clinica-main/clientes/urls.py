from django.urls import path
from . import views
from accounts import urls

app_name = 'clientes'

urlpatterns = [
    path('registro/', views.cliente_registro, name='cliente_registro'),
    path('atualizar/', views.cliente_atualizar, name='cliente_atualizar'),
    path('consultas/', views.consulta_lista, name='consulta_list'),
    path('consultas/crear/', views.consulta_registro, name='consulta_create'),
    path('consultas/editar/<int:pk>/', views.consulta_atualizar, name='consulta_update'),
    path('consultas/excluir/<int:pk>/', views.consulta_excluir, name='consulta_delete'),
    
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.join_room, name='join_room'),

]