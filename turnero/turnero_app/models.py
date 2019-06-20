from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from turnero.usuarios.models import User

from .task import task_notification

class Prioridad(models.Model):
    nombre = models.CharField(max_length=200)
    numero = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Prioridades"
        verbose_name = "Prioridad"

    def __str__(self):
        return "{} {}".format(self.nombre, self.numero)

class Servicios(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Servicio"
        verbose_name = "Servicios"

    def __str__(self):
        return "{}".format(self.nombre)

class ServiciosUsuarios(models.Model):
    servicicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    finalizo = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_finalización = models.DateTimeField(auto_now=True)
    inicio = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Turnos de usuarios"
        verbose_name = "Turnos de usuarios"

    def __str__(self):
        return "{} {} {}".format(self.pk,self.servicicios,self.usuario)

@receiver(post_save, sender=ServiciosUsuarios)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    task_notification.delay(instance.servicicios.pk)

class ServiciosEmpleado(models.Model):
    servicicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name='servicios_empleados')
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Servicios de los empleados"
        verbose_name = "Servicio de empleado"

    def __str__(self):
        return "{} {}".format(self.usuario,self.servicicios)


class TurnosEmpleados(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name='usuario_turnos')
    servicio = models.ForeignKey(ServiciosUsuarios, on_delete=models.CASCADE)
    proceso = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Turnos de los empleados"
        verbose_name = "Turno del empleado"

    def __str__(self):
        return "{} {}".format(self.usuario,self.servicio)
