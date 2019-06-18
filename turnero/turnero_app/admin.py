from django.contrib import admin

from .models import (
        Servicios,Prioridad,
        ServiciosUsuarios,ServiciosEmpleado,
        TurnosEmpleados,
    )

@admin.register(Servicios,ServiciosUsuarios,Prioridad,ServiciosEmpleado,TurnosEmpleados)
class AuthorAdmin(admin.ModelAdmin):
    pass