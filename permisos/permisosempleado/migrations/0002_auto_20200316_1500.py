# Generated by Django 3.0.4 on 2020-03-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisosempleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='numeroDias',
            field=models.IntegerField(),
        ),
    ]
