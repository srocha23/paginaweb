from django.contrib import admin
from personas.models import Persona, Domicilio , Producto , Categoria , ImagenProducto
# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class ProductosAdmin(admin.ModelAdmin):
    inlines = [
        ImagenProductoAdmin
    ]

admin.site.register(Persona)
admin.site.register(Domicilio)
admin.site.register(Producto)
admin.site.register(Categoria)

