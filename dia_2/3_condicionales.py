numero1 = 60
numero2 = 60

#   40     >    60    -> F
if numero1 > numero2:
    # Si la condicion se cumple
    print('en efecto se debe agregar a la BD')
elif numero1 == numero2:
    # Si la primera conficion no se cumple podemos hacer una segunda validcion
    print('No debemos hacer nada')
# elif ...
else:
    # Si la condicion no se cumple
    print('debemos solicitar los registros')

num_ventas = 30
if num_ventas >= 50:
    print('Dscto del 20%')
elif num_ventas >= 30:
    print('Dscto del 10%')
elif num_ventas >= 20:
    print('Dscto del 5%')
else:
    print('Dscto del 2%')



# Crear una funcion llamada resultado_final en la cual se reciba el nombre del alumno y su nota
# Si la nota es entre 20 y 18 entonces el alumno tiene felicitacion publica
# Si la nota es entre 15 y 17 el alumno esta aprobado y exonerado de la exposicion final
# Si la nota es entre 11 y 14 el alumno esta aprovabdo
# Si la nota es menor o igual que 10 entonces el alumno esta jalado

# Al final retornar un mensaje diciendo 'El alumno EDUARDO esta aprobado y exonerado de la expocision final' > 15 y 17
# deadline Miercoles 20/11 18:59:59

