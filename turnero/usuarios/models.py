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
    tipo_usuario = models.CharField(max_length=2,choices=TIPOS_USUARIOS,default=USUARIO)
    cedula = models.CharField(max_length=30,null=True,blank=True)
    OCUPADO = 'OC'
    DISPONIBLE = 'DI'
    ESTADO = [
        (OCUPADO, 'Ocupado'),
        (DISPONIBLE, 'Disponible'),
    ]
    estado = models.CharField(max_length=2,choices=ESTADO,default=DISPONIBLE)

    def get_turno(self):
        if len(self.usuario_turnos.all().filter(proceso=True)) == 0:
            self.estado = 'DI'
            self.save()
        else:
            return self.usuario_turnos.all().filter(proceso=True).order_by('-pk')
    
    def get_selected_turno(self):
        return self.usuario_turnos.all().filter(servicio__inicio=False,servicio__finalizo=False)[0]