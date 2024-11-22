-- Si queremos busfcar los alumnos por su correo y que el texto no sea sensible a mayus y minus
SELECT * FROM alumnos WHERE email ILIKE '%GmAiL%';

-- Si queremos buscar los alumnos cuyo correo contenga el texto gmail en cualquier posicion pero sensible a mayus y minus
SELECT * FROM alumnos WHERE email LIKE '%gmail%';

-- Mostrara todos los alumnos cuyo correo terminen en gmail
SELECT * FROM alumnos WHERE email LIKE '%gmail';

-- Mostrar todos los alumnos en cuya segunda posicion tengan la letra r
SELECT * FROM alumnos WHERE nombre ILIKE '__r%'

-- Mostrar todos los alumnos cuyo nombre tengan en la cuarta posicion la letra i y que terminen con la letra r
SELECT * FROM alumnos WHERE nombre ILIKE '___i%r'

-- Para realzar un ordenamiento utilizaremos la clausula ORDER BY y los valores son ASC / DESC
-- Mostrar todos los alumnos ordenado de manera ascendente
SELECT * FROM alumnos ORDER BY nombre  ASC;

-- Mostrar todos los alumnos ordenado de manera descendente
SELECT * FROM alumnos ORDER BY nombre  DESC;

SELECT * FROM alumnos ORDER BY nombre  DESC, email ASC;

-- Actualizara todos los nombres y apellidos de los alumnos cuyo id = 1
UPDATE alumnos SET nombre = 'Ramiro', apellidos = 'Perez' WHERE id = 1;

-- Eliminara a todos los alumnos que cumplan la condicion
DELETE FROM alumnos WHERE id = 1;