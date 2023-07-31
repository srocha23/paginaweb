from django.apps import AppConfig


class PersonasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personas'

class DomicilioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'domicilios'

class ProductoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'

class CategoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categoria'

