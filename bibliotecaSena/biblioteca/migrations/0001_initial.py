# Generated by Django 4.2.1 on 2023-05-16 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliNombre', models.CharField(db_comment='Nombre del cliente', max_length=50)),
                ('cliApellido', models.CharField(db_comment='Apellido del cliente', max_length=50)),
                ('cliNumeroTelefono', models.CharField(db_comment='Numero de telefono de contacto del cliente', max_length=15)),
                ('cliCorreo', models.EmailField(db_comment='Direccion del correo electronico del cliente', max_length=254)),
                ('cliDireccion', models.CharField(db_comment='Direccion fisica del cliente', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libTitulo', models.CharField(db_comment='Titulo del libro unico con el cual se identifca', max_length=50, unique=True)),
                ('libAutor', models.CharField(db_comment='Autor del libro', max_length=50)),
                ('libISBN', models.CharField(db_comment='Codigo unico asignado a cada libro para identificarlo', max_length=50, unique=True)),
                ('libGenero', models.CharField(choices=[('novela', 'novela'), ('ciencia ficcion', 'ciencia ficcion'), ('romance', 'romance'), ('historia', 'historia')], db_comment='Genero literario o tematica del libro', max_length=50)),
                ('libFechaPublicacion', models.DateField(db_comment='El año de publicacion por primera vez')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preCodigo', models.CharField(db_comment='Codigo unico del prestamo', max_length=50, unique=True)),
                ('preFechaPrestamo', models.DateTimeField(auto_now=True, db_comment='Corresponde a la fecha que el libro es retirado')),
                ('preFechaEntrega', models.DateTimeField(auto_now=True, db_comment='Fecha en la que el libro es regrsado')),
                ('estado', models.CharField(choices=[('En prestamo', 'En prestamo'), ('Devuelto', 'Devuelto')], max_length=20)),
                ('cliente', models.ForeignKey(db_comment='Llave foranea de relacion (prestamo-cliente)', on_delete=django.db.models.deletion.PROTECT, to='biblioteca.cliente')),
                ('libro', models.ForeignKey(db_comment='Llave foranea relacion(prestamo-libro)', on_delete=django.db.models.deletion.PROTECT, to='biblioteca.libro')),
            ],
        ),
    ]
