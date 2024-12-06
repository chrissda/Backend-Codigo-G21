from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
# Sera la encargada de gestionar todas las rutas de mi aplicacion
from flask_restful import Api 
from models import *
from controllers import *

# revisara si hay algun archivo llamado .env y leera las variables definidas en el y las colocara como variables de entorno
load_dotenv()

app = Flask(__name__)
api = Api(app)
# Si vamos a tener mas de una conexion a diferentes de base de datos, entonces debemos utilizar la variable SQLALCHEMY_BINDS
# Tengo que definir una conexion por defecto
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# si luego quiero agregar mas conexiones entonces las declarare en SQLALCHEMY_BINDS PERO aca ya no va la conexion por defecto
app.config['SQLALCHEMY_BINDS'] = {
    'postgres2': environ.get('DATABASE_URL2')
     # 'mysql': ''
}


# asi se puede inicializar la conexion a la base de datos desde otro archivo
conexion.init_app(app)
# al momento de crear nuestro modelo(tabla) usaremos las variable __bind_key__ para indicar a que base de datos queremos utilizar
# class UsuarioPostgresModel(conexion.Model):
#     __bind_key__='postgres'
#     id = Column(type_=types.Integer)

Migrate(app, conexion)

api.add_resource(CategoriaController, '/categorias')

if __name__ == '__main__':
    app.run(debug=True)