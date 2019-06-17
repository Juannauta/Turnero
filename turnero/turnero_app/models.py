from django.db import models

class Prioridad(models.Model):
    nombre = models.CharField(max_length=200)
    numero = models.IntegerField()

class Servicios(models.Model):
    nombre = models.CharField(max_length=200)

class ServiciosUsuarios(models.Model):
    servicicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Servicios de usuarios"
        verbose_name = "Servicios de usuarios"

    def __str__(self):
        return "{} {} {}".format(self.prioridad.nombre,self.servicicios.nombre,self.pk)