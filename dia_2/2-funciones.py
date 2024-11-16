def saludar():
    # Declarado el funcionamiento de la funcion saludar
    print('Buenas noches')
    print('Buenas tarde')
    print('Buenas dias')

# para ejecutar una funcion
saludar()

def saludar_bonito(nombre):
    print('Buenas noches', nombre)

saludar_bonito('Juanita')

def saludar_complejo(titulo, nombre, saludo):
    texto = saludo + ' ' + titulo + ' ' + nombre
    print(texto)

saludar_complejo('Jovencito', 'Juancito', 'Buen fin de semana')

# declara una funcio nque reciba n parametros
# args > argumentos
def mostrar_alumnos(*args):
    print(args)

mostrar_alumnos('Eduardo')
mostrar_alumnos('Luis', 'Francesca', 'Juan', 'Cristhian', 'Javier')
mostrar_alumnos('Arnold', 10, False, 8.5, {'nombre': 'Backend'})

# kwargs > Keyboard Arguments
# Es una funcion que recibira n parametros PERO con la definicion del nombre del parametro
def mostrar_info(**kwargs):
    print(kwargs)

mostrar_info(nombre='Gerardo', edad=30, aprobado=False, promedio_final=9.5)

# A una funcion tambien se le puede inficar que retorne un resultado, este puede ser cualquier cosa, es decirm un int, str, bool, o coleccion de datos u otra cosa
def sumar(numero1, numero2):
    return numero1 + numero2

resultado = sumar(40, 20)
print(resultado)

