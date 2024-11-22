psql -U postgres -h HOSTNAME -p PUERTO NOMBRE_DATABASE > conexion mas exacta para conectarnos a la bd

-- Asi se define un comentario en las bases de datos
-- DDL (Data Definition Language) es un sublenguaje de SQL para definir como se almacenaran los datos
CREATE DATABASE pruebas;

-- Limpiara la terminal de nuesto psql
-- \! cls

CREATE TABLE alumnos (
    id SERIAL NOT NULL PRIMARY KEY, -- Columna que sera autoincrementable, no puede ser nula y sera llave primaria
    nombre TEXT NOT NULL, -- Sera texto y no puede ser nula
    email TEXT NOT NULL UNIQUE, -- Sera texto, no puede ser nula y debe ser unica(no se repite)
    matriculado BOOLEAN DEFAULT true, -- Sera Booleana y su valor por defecto si no se ingresa sera TRUE
    fecha_nacimiento DATE NULL -- Sera fecha y puede tener valores nulos(su valor por defecto si no se define)
);

-- Para agregar columnas a una tabla ya existente
ALTER TABLE alumnos ADD COLUMN apellidos TEXT;

-- Cambiamos el tipo de dato de la columna nombre ahora sera VARCHAR(100)
-- NOTA: Solo se puede cambuar el tupo de dato si la comuna no tiene registros
-- o si ya tiene registros entonces el nuevo tipo de dato debe ser compatible con el antiguo
-- no podemos cambiar de un TEXT > INT o de un INT > FECHA
ALTER TABLE alumnos ALTER COLUMN nombre TYPE VARCHAR(100);

-- Elimnina de manera permanente e irreversible la tabla y toda la informacion que hay en ella
DROP TABLE direcciones;
DROP DATABASE NOMBRE_BD;


-- DML (Data Manupulation Language)
-- Es un sublenguaje para poder interactuar con al informacion de las tablas

-- Muestra la configuracion de la tabla con todas sus columnas y restricciones
-- \d alumnos


-- Insertamos un registro en la BD definiendo las columnas
INSERT INTO alumnos (id, nombre, email, matriculado, fecha_nacimiento, apellidos)
VALUES (DEFAULT, 'Cristhian', 'chrisscass@ggmail.com', TRUE, '1990-02-28', 'Barreto');

-- ALTER TABLE alumnos ADD CONSTRAINT alumnos_nombre_key UNIQUE(nombre)

-- Insertamos 2 o mas registros 
INSERT INTO alumnos VALUES (DEFAULT, 'Cesar', 'ccenteno@tecsup.edu.pe', DEFAULT, '1995-06-02', 'Centeno'), (DEFAULT, 'Javier', 'jwiesse@gmail.com', FALSE, '200-02-14', 'Wiesse'), (DEFAULT, 'Farit', 'fespinoza@gmail.com', TRUE, '1990-07-28', 'Espinoza');

-- Seleccionar una columna
SELECT nombre FROM alumnos;
-- Selecionar dos o mas columnas
SELECT id, nombre FROM alumnos;
-- Seleccionar todas las columnas
SELECT * FROM alumnos;

-- Agregar una condicion para filtrar datos
SELECT * FROM alumnos WHERE matriculado = FALSE;

-- Mostrara todos los alumnos que esten matriculaods y su id sea menor que 3
SELECT * FROM alumnos WHERE matriculado = TRUE AND id < 3;

-- Devolver todos los alumnos que esen matriculados y que su fecha de nacimiento sea el 1-01-1995
SELECT * FROM alumnos WHERE matriculado = TRUE AND fecha_nacimiento > '1995-01-01';

