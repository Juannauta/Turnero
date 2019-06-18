from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    USUARIO = 'US'
    EMPLEADO = 'EM'
    TIPOS_USUARIOS = [
        (USUARIO, 'Usuario'),
        (EMPLEADO, 'Empleado'),
    ]
    cedula = models.CharField(max_length=30,null=True,blank=True)
    tipo_usuario = models.CharField(max_length=2,choices=TIPOS_USUARIOS,default=USUARIO)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
