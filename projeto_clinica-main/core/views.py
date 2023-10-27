from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    
    def get(self, request):
        return render(request, 'index.html',)

class SaberMasView(View):
    template_name = 'sabermas.html'  # Nombre del archivo HTML que quieres mostrar en esta vista

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TerminosPrivacidadView(View):
    template_name = 'terminosprivacidad.html'  # Nombre del archivo HTML que deseas mostrar
    title = 'Términos y Privacidad'  # Título de la página

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': self.title})
