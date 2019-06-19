from django.db import models

from turnero.usuarios.models import User

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

    class Meta:
        verbose_name_plural = "Turnos de usuarios"
        verbose_name = "Turnos de usuarios"

    def __str__(self):
        return "{} {} {}".format(self.pk,self.servicicios,self.usuario)

class ServiciosEmpleado(models.Model):
    servicicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
