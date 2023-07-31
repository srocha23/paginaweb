    #path('detalle_persona/<int:id>', detallePersona),
    #path('nueva_persona', nuevaPersona),
    #path('editar_persona/<int:id>', editarPersona),
    #path('eliminar_persona/<int:id>', eliminarPersona),
    #path('catalogo', catalogo, name='cata'),
    #path('detalle_domi/<int:id>', domiDetalle),
    #path('nuevo_domi', nuevoDomi),
    #path('editar_domi/<int:id>', editarDomi),
    #path('eliminar_domi/<int:id>', eliminarDomi),

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from webapp.views import inicio,  listadoProductos
from personas.views import detalleProducto , formregistrar ,formactualizar, registrarProducto , nosotros



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index_inicio'),
    path('detalle_producto/<int:id>', detalleProducto),
    path('catalogo-index', listadoProductos),
    path('registrar_producto', formregistrar ),
    path('actualizar_producto', formactualizar ),
    path('insertar', registrarProducto ),
    path('nosotros_index', nosotros),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)