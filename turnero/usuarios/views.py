# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
        View, TemplateView, 
        UpdateView, CreateView,
        ListView,
    )

from turnero.turnero_app.models import (
        ServiciosUsuarios,TurnosEmpleados,
    )
from turnero.usuarios.models import User


class AcceptarServicio(LoginRequiredMixin,View):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        try:
            turno = ServiciosUsuarios.objects.get(pk=request.POST.get('turno',''))
        except:
            return HttpResponseRedirect(reverse('info'))

        turnoEmpleado = TurnosEmpleados(
            usuario=request.user,
            servicio=turno,
        )
        turnoEmpleado.save()
        request.user.estado = 'OC'
        request.user.save()
        return HttpResponseRedirect(reverse('info'))

class IndexView(TemplateView):
    template_name = "index.html"

class ListServices(ListView):
    model = ServiciosUsuarios
    queryset = ServiciosUsuarios.objects.filter(finalizo=False)


class RegisterUser(CreateView):
    model = ServiciosUsuarios
    fields = ('servicicios','prioridad','usuario',)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(cedula=self.request.POST.get('cedula',''))
        except:
            user = User(
                first_name=self.request.POST.get('first_name',''),
                last_name=self.request.POST.get('last_name',''),
                cedula=self.request.POST.get('cedula',''),
                username=self.request.POST.get('cedula',''),
            )
            user.save()
        self.object = None
        form = self.get_form()
        form.data = form.data.copy()
        form.data['usuario'] = str(user.pk)
        if form.is_valid():
            return self.form_valid(form)                
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('registro')

class UserLoginView(LoginView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse('info')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if form.get_user().tipo_usuario != "EM":
                return self.form_invalid(form)
            else:
                return self.form_valid(form)                
        else:
            return self.form_invalid(form)

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

class ListarInformacionUsuario(LoginRequiredMixin,UpdateView):
    template_name = "usuarios/listar_informacion_usuario.html"
    model = User
    fields = ('first_name','last_name','cedula',)

    def get_queryset(self):
        if self.request.user.estado == 'DI':
            self.pk = self.request.user.pk
            return self.request.user
        else:
            if self.request.user.get_turno() == None:
                return HttpResponseRedirect(reverse('info'))
            self.pk = self.request.user.get_turno()[0].usuario.pk
            return self.request.user.get_turno()[0].usuario

    def get_object(self, queryset=None):
        return self.get_queryset()

    def get_success_url(self):
        return reverse('info')

    def get_context_data(self, **kwargs):
        self.object = self.get_queryset()
        servicios = ServiciosUsuarios.objects.filter(finalizo=False).order_by('prioridad__numero')
        
        context = super().get_context_data(**kwargs)
        context.update({
            'turno':servicios,
        })
        return context
