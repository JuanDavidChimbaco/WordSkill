from django.contrib import admin
from biblioteca.models import *

# Register your models here.

admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Prestamo)