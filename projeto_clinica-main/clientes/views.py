from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente, Consulta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


class ClienteCreateView(LoginRequiredMixin ,CreateView):
    
    model = Cliente
    template_name = 'clientes/registro.html'
    fields = ['sexo', 'telefono', 'rut']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClienteUpdateView(LoginRequiredMixin, UpdateView):

    model = Cliente
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['sexo', 'telefono', 'rut']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        user = self.request.user
        try:
            return Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class ConsultaCreateView(LoginRequiredMixin, CreateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'clientes/registro.html'
    fields = ['agenda']
    success_url = reverse_lazy('clientes:consulta_list')
    
    def form_valid(self, form):
        try:
            form.instance.cliente = Cliente.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'No puedes realizar esta consulta')
                return HttpResponseRedirect(reverse_lazy('clientes:consulta_create'))
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Complete su registro')
            return HttpResponseRedirect(reverse_lazy('clientes:cliente_registro'))
        messages.info(self.request, '¡Consulta eliminada exitosamente!')
        return HttpResponseRedirect(reverse_lazy('clientes:consulta_list'))
    
class ConsultaUpdateView(LoginRequiredMixin, UpdateView):

    model = Consulta
    login_url = 'accounts:login'
    template_name = 'clientes/registro.html'
    fields = ['agenda']
    success_url = reverse_lazy('medicos:Consulta_lista')
    
    def form_valid(self, form):
        form.instance.cliente = Cliente.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    success_url = reverse_lazy('clientes:consulta_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "¡Consulta eliminada exitosamente!")
        return reverse_lazy('clientes:consulta_list')


class ConsultaListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'clientes/consulta_list.html'

    def get_queryset(self):
        user=self.request.user
        try:
            cliente = Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Crear una Consulta')
            return None
        try:
            consultas = Consulta.objects.filter(cliente=cliente).order_by('-pk')
        except Consulta.DoesNotExist:
            messages.warning(self.request, 'Crear una Consulta')
            return None
        return consultas
    
def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, 'registro.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'registro.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.username})

@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.username + " " })

@login_required
def logout_view(request):
    logout(request)
    return redirect("/registro")

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')

cliente_registro = ClienteCreateView.as_view()
cliente_atualizar = ClienteUpdateView.as_view()
consulta_lista = ConsultaListView.as_view()
consulta_registro = ConsultaCreateView.as_view()
consulta_atualizar = ConsultaUpdateView.as_view()
consulta_excluir = ConsultaDeleteView.as_view()
