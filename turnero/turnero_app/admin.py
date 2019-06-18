from django.contrib import admin

from .models import (
        Servicios,Prioridad,
        ServiciosUsuarios,ServiciosEmpleado,
    )

@admin.register(Servicios,ServiciosUsuarios,Prioridad,ServiciosEmpleado)
class AuthorAdmin(admin.ModelAdmin):
    pass