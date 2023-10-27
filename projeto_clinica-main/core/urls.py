from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import IndexView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('clientes/', include('clientes.urls', namespace="clientes")),
    path('medicos/', include('medicos.urls', namespace="medicos")),
    path('sabermas/', views.SaberMasView.as_view(), name='sabermas'),
    path('terminos-privacidad/', views.TerminosPrivacidadView.as_view(), name='terminos_privacidad'),

]
