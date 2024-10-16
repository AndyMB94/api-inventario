from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # Campo para ID automático
    nombre = models.CharField(max_length=100)  # Nombre del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    descripcion = models.TextField()  # Descripción del producto
    stock = models.IntegerField()  # Cantidad de stock disponible
    foto = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
