# Generated by Django 4.2 on 2023-04-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_entrenamiento_delete_clase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_comienzo', models.DateField()),
                ('asistencia', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='')),
                ('deporte', models.CharField(max_length=50)),
            ],
        ),
    ]