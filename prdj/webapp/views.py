from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from personas.models import Persona, Domicilio , Producto

# Create your views here.

def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas':no_personas, 'personas':personas})

def catalogo(request):
    no_domicilio = Domicilio.objects.count()
    domicilios = Domicilio.objects.order_by('id')
    return render(request, 'domicilio.html', {'no_domicilio':no_domicilio, 'domicilios':domicilios})

def inicio(request):

    return render(request, 'inicio.html')

def catalogo2(request):
    no_producto = Producto.objects.count()
    productos = Producto.objects.order_by('id')

    return render(request, 'catalogo.html', {'no_producto':no_producto, 'productos':productos})

def listadoProductos(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()

    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre_producto__icontains = busqueda) |
            Q(categoria__icontains = busqueda) |
            Q()
        )

    return render (request, "catalogo.html", {"productos": productos})