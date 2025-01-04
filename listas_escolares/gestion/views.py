from django.shortcuts import render, redirect
from .models import Producto

def mostrarProductosPlantilla(request):
    # request > toda la informacion deesde el navegador
    print(request)
    #SELECT * FROM productos;
    data = Producto.objects.all()
    
    # podemos retornar un html para cuestiones en que la aplicacion sea un monolito
    # https://jinja.palletsprojects.com/en/stable/
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje': 'Bienvenido!'})

def crearProductosFormulario(request):
    if request.method == 'POST':
        # Para recibir informacion proveniente del formulario en base a sus name
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        nuevoProducto = Producto(nombre = nombreProducto, descripcion = descripcionProducto)
        # Guarda el registro en la base de datos
        nuevoProducto.save()
        # Como en teoria ya se agrego mi producto en la base de datos entonces mandare un redireccionamiento a la vista de lista los productos
        return redirect('mostrar_productos')
    elif request.method == 'GET':
        return render(request, 'formulario_producto.html')