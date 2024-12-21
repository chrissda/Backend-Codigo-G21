from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Categoria
from marshmallow import fields
from .libro_serializer import LibroSerializer

class CategoriaSerializer(SQLAlchemyAutoSchema):
    # Si utilizamos un atributo que no esta debidamente identificado en el modelo, entonces tenemos que utilizar el parametro attribute
    libros = fields.Nested(
        LibroSerializer, many=True, attribute='libros')
    # Si tulizamos un atributo que ya esta siendo utlizado por otro elemento, lanzara un error, entonces debemos quitarlo


    class Meta:
        model = Categoria
        # si queremos que este serializador incluya las relaciones
        # include_relationships= True