from rest_framework.serializers import ModelSerializer
from .models import Producto

# Hay 2 formas de crear serializadores, la primera seria sun un model desde 0 como haciamos con marshmallow y la segunda utulizando un modelo
class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        # a diferencia de marshmallow tenemos qwue indicar que atributos vamos a utulizar del modelo
        # fields = ['id', 'nombre']
        # Si queremos utilizar los atributos
        fields = '__all__'
        # Otra forma de definir los atributos a utilizar seria
        # exclude = ['id', 'descripcion']
        # NOTA: no se puede utilizar los dos a la vez, es decir, o se usa el fields o se usar el exclude