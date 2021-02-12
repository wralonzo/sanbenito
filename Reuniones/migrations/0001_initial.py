# Generated by Django 2.2.1 on 2020-03-13 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Asistencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reuniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('Descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripción')),
                ('NombreMaestro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Asistencia.Maestro', verbose_name='Maestro')),
            ],
        ),
    ]
