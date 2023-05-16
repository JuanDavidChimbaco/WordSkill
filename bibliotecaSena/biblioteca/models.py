from django.db import models

# Create your models here.
"""_summary_
    Estos modelos crearan las bases de datos.
"""
generos = [
    ('novela','novela'),
    ('ciencia ficcion','ciencia ficcion'),
    ('romance','romance'),
    ('historia','historia')
]

estados = [
    ( 'En prestamo','En prestamo'),
    ('Devuelto','Devuelto')
]

class Libro(models.Model):
    libTitulo = models.CharField(max_length=50, unique=True, db_comment="Titulo del libro unico con el cual se identifca")
    libAutor = models.CharField(max_length=50, db_comment="Autor del libro")
    libISBN = models.CharField(max_length=50 ,unique=True ,db_comment="Codigo unico asignado a cada libro para identificarlo")
    libGenero = models.CharField(max_length=50, choices=generos ,db_comment="Genero literario o tematica del libro")
    libFechaPublicacion = models.DateField(auto_now=False, auto_now_add=False, db_comment="El año de publicacion por primera vez")
    def __str__(self) -> str:
        return self.libTitulo
    
class Cliente(models.Model):
    cliNombre = models.CharField(max_length=50, db_comment="Nombre del cliente")
    cliApellido = models.CharField(max_length=50, db_comment="Apellido del cliente")
    cliNumeroTelefono = models.CharField(max_length=15, db_comment="Numero de telefono de contacto del cliente")
    cliCorreo = models.EmailField(max_length=254,db_comment="Direccion del correo electronico del cliente")
    cliDireccion = models.CharField(max_length=50, db_comment="Direccion fisica del cliente")
    def __str__(self) -> str:
        return self.cliNombre
    
class Prestamo(models.Model):
    preCodigo = models.CharField(max_length=50, unique=True, db_comment="Codigo unico del prestamo")
    preFechaPrestamo = models.DateTimeField(auto_now=True, db_comment="Corresponde a la fecha que el libro es retirado")
    preFechaEntrega = models.DateField(auto_now=False , db_comment="Fecha en la que el libro es regrsado")
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT, db_comment="Llave foranea relacion(prestamo-libro)")
    cliente = models.ForeignKey(Cliente , on_delete=models.PROTECT, db_comment="Llave foranea de relacion (prestamo-cliente)")
    estado = models.CharField(max_length=20 , choices=estados)
    def __str__(self) -> str:
        return f"{self.preCodigo} - {self.libro} - {self.cliente} - {self.estado}"
    