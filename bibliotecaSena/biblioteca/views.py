from django.shortcuts import render
from biblioteca.models import *
from django.db import Error
import os
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def vistaLibros(request):
    libro = Libro.objects.all()
    retorno = {"listaLibros":libro}
    return render(request, 'frmAgregarLibros.html', retorno)

def vistaPrestamos(request):
    libro = Libro.objects.all()
    retorno = {"listaLibros":libro}
    return render(request, 'frmAgregarPrestamos.html', retorno)

def vistaClientes(request):
    libro = Cliente.objects.all()
    retorno = {"listaLibros":libro}
    return render(request, 'frmAgregarClientes.html', retorno)

def agregarLibros(request):
    titulo = request.POST['txtTitulo']
    autor = request.POST['txtAutor']
    codigo = request.POST['txtISBN']
    genero = int(request.POST['cbGenero'])
    fechaPublicacion = request.POST['txtFechaPublicacion']
    try:
        libro = Libro(libTitulo=titulo,libAutor=autor,libISBN=codigo,libGenero=genero,libFechaPublicacion = fechaPublicacion)
        libro.save()
        mensaje="Libro Agregado Correctamente"
    except Error as error:
        mensaje=f"Problemas a la hora de agregar la libro{error}"
    retorno = {"mensaje":mensaje}
    return render(request,"inicio.html",retorno)

def agregarClientes(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    correo = request.POST['txtCorreo']
    direccion = request.POST['txtDireccion']
    try:
        cliente = Cliente(cliNombre=nombre,cliApellido=apellido,cliNumeroTelefono=telefono,cliCorreo=correo,cliDireccion = direccion)
        cliente.save()
        mensaje="Cliente Agregado Correctamente"
    except Error as error:
        mensaje=f"Problemas a la hora de agregar la cliente{error}"
    retorno = {"mensaje":mensaje}
    return render(request,"inicio.html",retorno)

def agregarPrestamos(request):
    codigo = request.POST['txtCodigo']
    fechaPrestamo = request.POST['txtFechaPestamo']
    fechaEntrega = request.POST['txtFechaEntrega']
    libro = request.POST['txtLibro']
    cliente = request.POST['txtcliente']
    estado = int(request.POST['cbEstado'])
    try:
        libro = Libro.objects.get(libTitulo=libro)
        cliente = Cliente.objects.get(cliNombre = cliente)
        prestamo = Prestamo(preCodigo=codigo,preFechaPrestamo=fechaPrestamo,
                            preFechaEntrega=fechaEntrega,libro=libro,cliente = cliente)
        libro.save()
        mensaje="prestamo Agregado Correctamente"
    except Error as error:
        mensaje=f"Problemas a la hora de agregar el prestamo{error}"
    retorno = {"mensaje":mensaje}
    return render(request,"inicio.html",retorno)


def listaReporte(request):
    try:
        reporte = Prestamo.objects.all()
        mensaje = ""
        print(reporte)
    except Error as error:
        mensaje=f"Problemas al obtener Productos {error}"
    retorno={"mensaje":mensaje,"listaReporte":reporte}
    return render(request,'reporte.html',retorno)