from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# 
from sqlalchemy import Column, types

app = Flask(__name__)

# Aca agregamos la variable de conexxion a nuestra base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:0987@localhost:5432/bd_flask'
conexion = SQLAlchemy(app=app)

# Cada tabla que vayamos a crear sera como una clase
class ProductoModel(conexion.Model):
    # Herencia: Semana 1 Programacion Orientada a Objetos
    # Ahora declaramos las columnas de la tabla como si fueran atributos de la clase

    # id ....serial primary key > SQL
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    # nombre ....not null, > SQL
    nombre = Column(type_=types.Text, nullable=False)
    # precio .... not null > SQL
    precio = Column(type_=types.Float(precision=2), nullable=False)
    # serie = ...not null unique > SQL
    serie = Column(type_=types.Text, nullable=False, unique=True)
    disponible = Column(type_=types.Boolean, nullable=True)

@app.route('/crear-tablas')
def crear_tablas():
    # Creara todas las tablas que no esten en la BD
    # Si la tabla ya existe no la creara aun asi dentro de la tabla tenga modificaciones como agregar columna, quitar columna, relaciones, etc
    # SIGUIENTE PASO: Usar migraciones
    conexion.create_all()
    return {
        'message': 'Las tablas fueron creadas exitosamente'
    }

app.run(debug=True)