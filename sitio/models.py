from django.db import models
from django.contrib import admin

#TABLA INGREDIENTE
class Ingrediente(models.Model):
    """Model definition for Ingrediente."""
    nombre = models.CharField(max_length=50)
    class Meta:
        """Meta definition for Ingrediente."""

        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        """Unicode representation of Ingrediente."""
        return self.nombre

#TABLA CLIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=254)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return self.nombre

#TABLA BEBIDA
class Bebida(models.Model):
    """Model definition for Bebida."""

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente, through='DetalleBebida')

    class Meta:
        """Meta definition for Bebida."""

        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

    def __str__(self):
        """Unicode representation of Bebida."""
        return str(self.pk)

#TABLA DETALLEBEBIDA

class DetalleBebida (models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)

class DetalleBebidaInLine(admin.TabularInline):
    model = DetalleBebida
    extra = 1


class IngredienteAdmin(admin.ModelAdmin):
    inlines = (DetalleBebidaInLine,)


class BebidaAdmin (admin.ModelAdmin):
    inlines = (DetalleBebidaInLine,)