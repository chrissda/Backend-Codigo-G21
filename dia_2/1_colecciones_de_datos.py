# listas (Arreglos o Arrays)
# Ordenada y editable
frutas = ['Manzana', 'Platano', 'Papaya', 'Pitahaya']

# Ordenando > Cada elemento de la lista esta en una POSICION determinada
print(frutas[1])

# Editable . agregar y eliminar elemntos de la lista
frutas.append('Mandarina')
frutas.append('Piña')

print(len(frutas))

# frutas.remove('Platano')
print(frutas)
# el metodo remove solamente si existe ese elemento lo eliminara, sino , lanzara un error
# frutas.remove('Aguaymanto')

# el metodo pop funciona con la POSICION de la fruta
frutas.pop(0)
print(frutas)

# Reemplazando el valor antiguo por un nuevo valor
frutas[0] = 'Kiwi'
print(frutas)

# Colocando como primer parametro el indice donde se agregara el nuevo contenido y como segundo parametro el contenido a agregar
frutas.insert(2, 'Uva')
print(frutas)

usuario = ['Eduardo', 'de Rivero',
           'ederiveroman@gmail.com', '1992/08/01', False, 1.50, ['Nadar', 
           'Programar', 'Montar bici']]

# Tuplas
# No son EDITABLES! Una vez creada ya no pueden modificar
# Son Ordenadas
alumnos = ('Farit', 'Francesca', 'Cesar', 'Cristhian', 'Eddy')

print(alumnos[0])

# Otra forma de crear una lista en base a una tupla PERO la tupla original sigue siendo una tupla que no se puede editar
copia_alumnos = list(alumnos)
print(id(alumnos))
print(id(copia_alumnos))

copia_alumnos[0] = 'Briggit'
print(copia_alumnos)

segunda_copia = tuple(copia_alumnos)
print(id(segunda_copia))
# segunda_copia[0] = 'Pedro'

# Cuando copiamos una lista a otra variable lo que estamos en realida es utilizar la misma posicion de memoria
# Ahora hago una copia del contenido y esto indica que se guarde en otra posicion de memoria
otra_frutas = frutas[:]
print(id(otra_frutas))
print(id(frutas))

print(otra_frutas)

frutas[1]='Fruta del dragon'
print(otra_frutas)

# SET (Conjunto)
# Es DESORDENADA
# Es EDITABLE
inventario = {
    'Monitores',
    'Mouse',
    'Proyectores',
    'Ventiladores',
    'Teclados'
}

print(inventario)
# No se puede realizar porque no es una coleccion de datos ordenada
# print(inventario[0])
inventario.add('Memoria RAM')
inventario.remove('Mouse')
print(inventario)

print('Monitores' in inventario)
print('Laptops' in inventario)


# DICCIONARY - DICCIONARIOS
# Ordenado PERO POR LLAVES no por posicion ni indices
# Editable

persona = {
    'nombre': 'Eduardo',
    'apellido': 'de Rivero',
    'correo': 'ederivero@gmail.com',
    'hobbies': ['Comer', 'Programar', 'Montar bici'],
    'direcciones': {
        'calle': 'Calle los geranios',
        'numero': 870,
        'postal': '04010'
    },
    'viudo': False,
    'familiares': ('Juanuto Perez', 'Maria Aguilar', 'Roxana Washington')
}

print(persona['nombre'])

# Quiero ver los hobbies de la persona
print(persona['hobbies'])

# Quiero ver cuantos hobbies tiene la persona (numeros)
print(len(persona['hobbies']))

# Quiero ver en que calle vive la persona
print(persona['direcciones']['calle'])

# Quiero saber si es viudo o no
print(persona['viudo'])
print(persona.get('viudo'))

# Quiero saber si Maria Washington es su familiar o no
print('Maria Whashington' in persona['familiares'])


curso = {
    'nombre': 'Backend',
    'duracion': '10 semanas',
    'fecha_inicio': '2024-11-11',
    'fecha_fin': '2025-01-30',
    'topics': ['Python', 'Express', 'Django', 'Flask'],
    'semanas': [
        {
            'nombre': 'semana 01',
            'descripcion': 'intro a python'
        },
        {
            'nombre': 'semana 02',
            'descripcion': 'base de datos'
        }
    ],
    'habilidades': ('logica de programacion', 'manejo de eventos', 'despliegue en servidores'),
    'finalizado': False,
    'profesores': {
        'Arnold Gallegos', 'Eduardo de Rivero'
    },
    'costo': 550.76,
    'descanso': 'a veces'
}