# Generated by Django 2.2.2 on 2019-06-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnero_app', '0012_auto_20190619_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnosempleados',
            name='inicio',
        ),
        migrations.AddField(
            model_name='serviciosusuarios',
            name='inicio',
            field=models.BooleanField(default=True),
        ),
    ]