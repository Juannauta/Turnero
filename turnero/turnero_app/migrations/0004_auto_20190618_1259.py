# Generated by Django 2.2.2 on 2019-06-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnero_app', '0003_auto_20190618_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciosusuarios',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='serviciosusuarios',
            name='fecha_finalización',
            field=models.DateTimeField(null=True),
        ),
    ]
