from flask import Flask, request
from psycopg import connect

# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos es el archivo principal (el que sese esta ejecutando por la terminal). Si es el archivo principal su valor sera '__main__', caso contrario tendra otro valor variable
app = Flask(__name__)
# Flask solo puede tener una instancia en todo el proyecto y esa instancia debe de estar en el archivo principal, sino no podrea ejecurtarse la instancia de la clase

# Para conectarse a la bd:
# Formato standar para la conexion a las bd
# DIALECTO = //USUARIO:PASSWORD@HOST:PUERTO/DATABASE_NAME
conexion = connect(conninfo='postgresql://postgres:0987@localhost:5432/finanzas')

# Mediante el uso de decoradores podemos indicar la ruta y cual sera su comportamiento
# Un decorador sirve para poder reusar el metodo de una clase pero sin la necesidad de editarlo como tal, solo se modificara el funcionamiento para, en este caso, la ruta configurada
@app.route('/')
def inicio():
    return 'Bienvenido a mi aplicacion de Flask!'

@app.route('/inicio', methods = ['POST'])
def inicio_aplicacion():
    return {
        'message': 'Buenas noches, acabas de descubrir otro endpoint'
    }

# Si queremos recibir un parametro por la url que sea dinamico, este parametro tiene que estar entre < >, adicional a ello se puede indicar el tipo de dato (int, string)
@app.route('/usuarios/<int:id>', methods=['GET', 'POST'])
def mostrar_usuario(id):
    # cuando podemos un parametro dinamico entonces ese parametro tiene que ser registrado con el mismo nombre como parametro de la funcion
    print(id)
    return {
        'message': f'El usuario es {id}'
    }

@app.route('/gestionar-usuario/<int:id>', methods=['POST', 'PUT', 'DELETE'])
def gestionar_usuario(id):
    # para poner manejar la informacion de la peticion se usa el metodo request de flask
    if request.method == 'POST':
        return {
            'message': 'La creacion del usuario fue exitosa'
        }
    elif request.method == 'PUT':
        return {
            'message': 'Usuario actualizado exitosamente'
        }
    elif request.method == 'DELETE':
        return {
            'message': 'Usuario eliminado exitosamente'
        }

@app.route('/listar-clientes', methods=['GET'])
def listar_clientes():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    # Para obtener la informacion proveniente de select
    # fetchall() > devuelve todos los registros del select
    # fetchmany(limite) > devuelve los regstros hasta el limite
    # fetchone() > devuelve el primer registro del select
    data = cursor.fetchall()
    
    resultado = []

    for registro in data:
        informacion_cliente = {
            'id': registro[0],
            'nombre': registro[1],
            'correo': registro[2],
            'status': registro[3],
            'activo': registro[4],
            'fecha_creacion': registro[5]
        }
        print(informacion_cliente)
        resultado.append(informacion_cliente)
    
    return {
        'message': 'Los clientes son',
        'content': resultado
    }

# Crear un ENDPOINT en el cual sira para devolver un cliente por su ID
# /cliente/1 > Rodrigo

@app.route('/cliente/<int:id>', methods=['GET'])
def devolver_cliente(id):
    # Primero me conecto a la BD
    cursor = conexion.cursor()
    # Ejecuto la consulta para obtener el cliente
    cursor.execute(f'SELECT * FROM clientes WHERE id = {id}')
    # fetchone porque solo queremos ubicar 1 cliente
    cliente_encontrado = cursor.fetchone()
    # None es null significa no hay datos
    if cliente_encontrado is None:
        return {
            'message': 'El cliente no existe'
        }
    resultado = {
        'id': cliente_encontrado[0],
        'nombre': cliente_encontrado[1],
        'correo': cliente_encontrado[2],
        'status': cliente_encontrado[3],
        'activo': cliente_encontrado[4],
        'fecha_creacion': cliente_encontrado[5]
    }
    return {
        'message': 'Usuario encontrado',
        'content': resultado
    }


# Toda la funcionalidad de nuestro servidor tiene que ir antes del metodo .run
# levanta el servidor de Flask con algunos parametros opcionales
# debug > si su valor es True entonces cada vez que modifiquemos el servidor y guardemos este se reiniciara automaticamente
app.run(debug=True)