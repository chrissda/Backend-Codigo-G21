from django.shortcuts import render, redirect
from .models import Producto
# Utilizando django rest framework puedo agregar endpoints como en flask
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductoSerializer


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


@api_view(http_method_names=['GET','POST'])
def validarFuncionamiento(request):
    # Este es un request diferente al de las plantillas porque se usa de la libreria
    # https://www.django-rest-framework.org/api-guide/requests/
    if request.method == 'GET':
        # En DRF no se puede retornar una plantilla sino que se tiene qe retornar una repuesta http y para que se pueda utilizar la clase Response
        return Response(data={
            'message': 'El servidor funciona exitosamente'
        })
    elif request.method == 'POST':
        # Para leer la informacion proveniente del body usamos el request.data
        print(request.data)
        return Response(data={
            'message': 'Informacion aceptada correctamente'
        })
    
# Al usar GenericApiView esto es muy similar a como lo haciamos en flask usando la clase Resource
class ProductosController(GenericAPIView):
    def get(self,request):
        # SELECT * FROM productos;
        productos = Producto.objects.all()
        # Al momento de crear la instancio del serializador se le pasa la informacion y si es una lista se le coloca el parametro many=True para que lo pueda iterar
        serializador = ProductoSerializer(productos,many=True)
        # si la informacion es correctamente serializada retornada la data
        serializador.data
        return Response(data={
            'message': 'Los productos son:',
            'content': serializador.data
        })
    def post(self, request):
        # la data proviene del request
        data = request.data
        serializador = ProductoSerializer(data=data)
        # ahora como queremos validar si esta informacion del cliente es valida usamos el metro is_valid()
        if serializador.is_valid():
            # Usando model serializes es muy facil guardar la informacion en al BD
            # Aca la data ya es valida para guardarse
            serializador.save()
            return Response(data={
            'message': 'Producto creado exitosamente'
            })
        else:
            # Si no es valida
            # si la informacion no es valida, los campos del porque no lo es se guardara en el atributo errors
            return Response(data={
            'message': 'Error al crear el producto',
            'content': serializador.errors
            })


class ListarYCrearProductosController(ListCreateAPIView):
    # Para utilizar una vista generica se tiene que definir los siguientes atributos
    # Como obtendra la informacion y la devolvera
    queryset = Producto.objects
    # Para indicar como tien que validar y devolver la informacion proveniente de la bd
    serializer_class = ProductoSerializer

class DevolverActualizarEliminarProductosController(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects
    serializer_class = ProductoSerializer
    # Si cambiamos el nombre del parametro en nuestra url
    lookup_field = 'id'