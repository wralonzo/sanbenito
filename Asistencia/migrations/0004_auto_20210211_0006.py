# Generated by Django 2.2.12 on 2021-02-11 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencia', '0003_auto_20210210_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='NombreAlumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Asistencia.Alumno', verbose_name='Alumno'),
        ),
    ]