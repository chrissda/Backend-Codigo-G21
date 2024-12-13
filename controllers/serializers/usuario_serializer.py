from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import Usuario, TipoUsuario
from marshmallow_enum import EnumField
from marshmallow import Schema, fields

class RegistroSerializer(SQLAlchemyAutoSchema):
    # Si quiero modificar alguna columna del modelo para cuestiones del serializador
    # Ahora modificamos la columna password y le indicamos que tiene que ser requerida a la hora de serializar
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Field
    # https://marshmallow-sqlalchemy.readthedocs.io/en/stable/api_reference.html#marshmallow_sqlalchemy.auto_field
    password = auto_field(required=True, load_only=True)
    # modificar el comportamiento de la columna que sea enum en la cual se le coloca que enum debve utulizar para hacer las validaciones correspondientes
    tipo_usuario = EnumField(TipoUsuario)

    class Meta:
        model = Usuario

class LoginSerializer(Schema):
    correo = fields.Email(required=True)
    password = fields.String(required=True)