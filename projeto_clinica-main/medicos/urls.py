from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('registro/medico/', views.medico_registro, name='medico_registro'),
    path('registro/especialidad/', views.especialidad_registro, name='especialidad_registro'),
    path('agendar/', views.agenda_registro, name='agendar_consulta'),
    path('agendar/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_consulta_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),
    path('mis/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/medicos/', views.medico_lista, name="medicos_lista"),
    path('admim/lista/especialidades/', views.especialidad_lista, name="especialidad_lista")
    
]