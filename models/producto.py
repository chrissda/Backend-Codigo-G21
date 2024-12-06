# ProductoModel
# id Integer, pk, autoincrementable
# nombre TEXT no puede ser null
# precio Float y no puede ser null
# disponibilidad Boolean y su valor por defecto va a ser True

# nombre de la tabla sea 'Productos'
# ademas agregar el bind_key
from instancias import conexion
from sqlalchemy import Column, types, ForeignKey

class ProductoModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=True)
    descripcion = Column(type_=types.Text)
    precio = Column(type_=types.Float, nullable=False)
    disponibilidad = Column(type_=types.Boolean, default=True)

    # RELACIONES
    # En este caso estariamos utilizando una relacion de 1 a m
    categoriaId = Column(ForeignKey(column='categorias.id'),
                         type_=types.Integer, nullable=False)

    __tablename__ = 'productos'
    __bind_key__ = 'postgres2'

    