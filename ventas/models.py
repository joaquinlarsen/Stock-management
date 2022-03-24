from django.db import models
from django.utils import timezone
from productos.models import Producto

# Create your models here.


class Venta(models.Model):
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    cantidad_vendida = models.PositiveIntegerField()
    precio_total = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True)
    nota = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad_vendida
        if self.fecha is None:
            self.fecha = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.cantidad_vendida} {self.producto.nombre} {self.producto.presentacion}"
