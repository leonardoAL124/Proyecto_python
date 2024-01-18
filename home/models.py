from django.db import models

# Create your models here.
class Benefits(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Beneficio")
    description = models.TextField(verbose_name = "Descripción")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Beneficio"
        verbose_name_plural = "Beneficios"
        ordering = ['title']

    def __str__(self):
        return self.title

class Display_products(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    qualification = models.IntegerField(verbose_name = "Calificación")
    stock = models.IntegerField(verbose_name = "Stock")
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Precio")
    image = models.ImageField(upload_to = "home_prods", blank=True, null=True, verbose_name = "Imagen")
    benefit = models.ManyToManyField(Benefits, verbose_name = "Beneficios")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Producto en exhibición"
        verbose_name_plural = "Productos en exhibición"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def range(self):
        return range(self.qualification)

class Indications(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Indicación")
    description = models.TextField(verbose_name = "Descripción")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Indicación"
        verbose_name_plural = "Indicaciones"
        ordering = ['title']

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Titulo")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(upload_to = "home_blog", blank=True, null=True, verbose_name = "Imagen")
    url = models.URLField(blank=True, null=True,  verbose_name = "Enlace")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['title']

    def __str__(self):
        return self.title