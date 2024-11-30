from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# 
from sqlalchemy import Column, types
from flask_migrate import Migrate

app = Flask(__name__)

# Aca agregamos la variable de conexxion a nuestra base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:0987@localhost:5432/bd_flask'

conexion = SQLAlchemy(app=app)

# Luego de establecer la conexion utilizando SQLAlchemy ahora utilizamos la clase Migrate
Migrate(app=app, db=conexion)

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
    # name > si queremos manejar un nombre en el backend y otro nombre en la bd con la propiedad name indicamos como se llamara en la bd
    fecha_vencimiento = Column(type_=types.Date, nullable=True, name='fecha_vencimiento')

    __tablename__ = 'productos'

# @app.route('/crear-tablas')
# def crear_tablas():
#     # Creara todas las tablas que no esten en la BD
#     # Si la tabla ya existe no la creara aun asi dentro de la tabla tenga modificaciones como agregar columna, quitar columna, relaciones, etc
#     # SIGUIENTE PASO: Usar migraciones
#     conexion.create_all()
#     return {
#         'message': 'Las tablas fueron creadas exitosamente'
#     }

@app.route('/productos', methods=['POST', 'GET'])
def gestion_productos():
    metodo = request.method
    if metodo == 'POST':
        # primero leeremos la informacion proveniente del cliente
        # Convierte el json entrante a un diccionario para que pueda ser leido en python
        data = request.get_json()
        
        # Inicializamos nuestro nuevo registro
        nuevoProducto = ProductoModel(nombre = data.get('nombre'), 
                        precio=data.get('precio'), 
                        serie=data.get('serie'), 
                        disponible=data.get('disponible'), 
                        fecha_vencimiento=data.get('fechaVencimiento'))
        print('Producto antes de guardarse en la bd', nuevoProducto.id)
        # utilizamos la conexion para conectarnos a la bd
        # empezamos una transaccion en la cual estamos indicando que agregaremos este registro
        conexion.session.add(nuevoProducto)

        # indicamos que los cambios tiene que guardarse de manera permanente
        conexion.session.commit()

        return {
            'message': 'Producto creado exitosamente'
        }
    elif metodo == 'GET':
        # Establecemos una consulta de obtencion de datos
        productos = conexion.session.query(ProductoModel).all()

        print(productos)
        return {
              'message': 'Los productos son: '
        }

if __name__ == "__main__":
    app.run(debug=True)