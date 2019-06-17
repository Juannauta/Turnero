from django.contrib import admin

from .models import (
        Servicios,Prioridad,ServiciosUsuarios
    )

@admin.register(Servicios,ServiciosUsuarios,Prioridad)
class AuthorAdmin(admin.ModelAdmin):
    pass