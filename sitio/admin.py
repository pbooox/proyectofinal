#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.

from django.contrib import admin
from sitio.models import Ingrediente, Cliente, Bebida, IngredienteAdmin, BebidaAdmin

#Registramos nuestras clases principales.

admin.site.register(Cliente)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Bebida, BebidaAdmin)
