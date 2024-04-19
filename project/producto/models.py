from django.db import models

class ProductoCategoria(models.Model):
    """Caregorias de productos"""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripcion")

    def  __str__(self) -> str:
        """Respresenta una instancia del modelo como una cadena de texto"""
        return self.nombre
    
    class Meta:
        verbose_name = "categoria de productos"
        verbose_name_plural = "categorias de productos"
 