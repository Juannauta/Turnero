# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


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
            print(form.get_user().tipo_usuario)
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

class ListarInformacionUsuario(LoginRequiredMixin,TemplateView):
    template_name = "usuarios/listar_informacion_usuario.html"
