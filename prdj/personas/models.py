from autoslug import AutoSlugField
from django.db import models

# Create your models here.



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    cate1 = 'Relojes hombre'
    cate2 = 'Relojes mujer'
    cate3 = 'Locines hombre'
    cate4 = 'Lociones mujer'
    categorias = (
        (cate1, 'Relojes hombre'),
        (cate2, 'Relojes mujer'),
        (cate3, 'Locines hombre'),
        (cate4, 'Lociones mujer'),
    )
    nombre = models.CharField(max_length=250, choices=categorias)
    slug=AutoSlugField(populate_from='nombre')

    def __str__(self) :
        return self.nombre


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    nombre_producto = models.CharField(max_length=250)
    slug=AutoSlugField(populate_from='nombre_producto')
    precio = models.DecimalField(max_digits=15,decimal_places=2,default=0.0)
    descripcion = models.CharField(max_length=250)
    disponible = 'Disponible'
    agotado = 'Agotado'
    Disponible = (
        (disponible, 'Disponible'),
        (agotado, 'Agotado'),
    )
    stock = models.CharField(max_length=250, choices=Disponible)
    destacado=models.BooleanField(default=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True)


    def __str__(self) :
        return f'Producto {self.id}: {self.nombre_producto} {self.imagen}'
        #return self.nombre_producto

class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to='img/')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


class Domicilio(models.Model):
    calle = models.CharField(max_length=250)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=250)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.nombre
