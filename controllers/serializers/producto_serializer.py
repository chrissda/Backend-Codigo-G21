from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import ProductoModel

class ProductoSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        # Para indicar al serializador que tambien haga la validacion de las columnbas que son llaves foarenas (FK), su valor por defecto es False
        include_fk = True