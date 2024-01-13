from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    qualification = models.IntegerField(verbose_name = "Calificación")
    stock = models.IntegerField(verbose_name = "Stock")
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Precio")
    image = models.ImageField(upload_to = "home_prods", blank=True, null=True, verbose_name = "Imagen")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def range(self):
        return range(self.qualification)