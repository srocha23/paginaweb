
from django.shortcuts import render, get_object_or_404, redirect
from personas.models import Persona, Domicilio , Producto , Categoria , ImagenProducto
#from django.forms import modelform_factory
from personas.forms import PersonaForm , DomicilioForm , CategoriaForm, ProductoForm

# Create your views here.

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance = persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

def domiDetalle(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilio/detalled.html', {'domicilio':domicilio})

def nuevoDomi(request):
    if request.method == 'POST':
        formaDomi = DomicilioForm(request.POST)
        if formaDomi.is_valid():
            formaDomi.save()
            return redirect('cata')
    else:
        formaDomi = DomicilioForm()
    return render(request, 'domicilio/nuevod.html', {'formaDomi':formaDomi})

def editarDomi(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomi = DomicilioForm(request.POST, instance = domicilio)
        if formaDomi.is_valid():
            formaDomi.save()
            return redirect('cata')
    else:
        formaDomi = DomicilioForm(instance=domicilio)

    return render(request, 'domicilio/editard.html', {'formaDomi':formaDomi})

def eliminarDomi(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('cata')

def detalleProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)

    return render(request, 'productos/detallep.html', {'producto':producto})

def formregistrar(request):
    formaProducto = ProductoForm(request.POST)
    return render(request, 'productos/registrar2.html', {'formaProducto':formaProducto})


def registrarProducto(request):

    if request.method == 'POST':
        #formaProducto = ProductoForm(request.POST)
        nom = request.POST['nombre_producto']
        fot = request.FILES['imagen']
        pre = request.POST['precio']
        desc =request.POST['descripcion']
        sto = request.POST['stock']
        cat = request.POST['categoria_id']
        comprobarNombre = Producto.objects.filter(nombre_producto = nom)
        if comprobarNombre:
            datos = {'r2': 'Duplicado ('+str(nom)+') Ya Existe'}
            #return redirect('productos/registrar2.html')
            return render(request, 'productos/registrar2.html', {'datos':datos})
            #return render(request, 'productos/registrar2.html', {'datos':datos})
        else:
            pel = Producto(nombre_producto=nom, imagen=fot, precio=pre, descripcion=desc, stock=sto, categoria_id=cat )
            pel.save()
            datos = {'r':'Producto ('+str(nom)+') registrado'}
            return render(request, 'productos/registrar.html', {'datos':datos})
            #return redirect('productos/registrar2.html')
           # return render(request, 'productos/registrar2.html', {'datos':datos})

    else:
        datos = {'r2': 'No se puede'}
        formaProducto = ProductoForm()
    return render(request, 'productos/registrar2.html')
   #return render(request, 'productos/registrar2.html',{'formaProducto':formaProducto, 'datos':datos})


def formactualizar(request):

    return render(request, 'productos/actualizar.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def editarDomi(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomi = DomicilioForm(request.POST, instance = domicilio)
        if formaDomi.is_valid():
            formaDomi.save()
            return redirect('cata')
    else:
        formaDomi = DomicilioForm(instance=domicilio)

    return render(request, 'domicilio/editard.html', {'formaDomi':formaDomi})


#def formactualizar(request):
    #producto = get_object_or_404(Producto, pk=id)
    #if request.method == 'POST':
        #formaProd = CategoriaForm(request.POST, instance=producto)
       # if #formaProd.is_valid():
            #formaProd.save()
            #return redirect('catalogo-index')
        
        #else:
            #formaProd = CategoriaForm(intance=producto)

    #return render(request, 'productos/actualizar.html' , {'formaProd':formaProd})