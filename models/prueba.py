from instancias import conexion
from sqlalchemy import Column, types

class PruebaModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text)

    # Al no definir el atributo __bind_Key__ este creara en la base de datos por defecto(SQLALCHEMMY_DATABASE_URI)
    # solamente se debe definir el __bind_key__ en las tablas que queremos crear en las otras conexiones
    __tablename__ = 'pruebas'