# Generated by Django 2.2.2 on 2019-06-18 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnero_app', '0007_auto_20190618_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='prioridad',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='servicios',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='serviciosempleado',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='TurnosEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proceso', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnero_app.ServiciosUsuarios')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Turno del empleado',
                'verbose_name_plural': 'Turnos de los empleados',
            },
        ),
    ]
