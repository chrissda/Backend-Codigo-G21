-- USAR LA BD prueba
CREATE TABLE demostracion_triggers (
    id SERIAL PRIMARY KEY NOT NULL,
    mensaje TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE FUNCTION registrar_accion()
RETURNS TRIGGER AS $$
BEGIN
-- Insertar un mensaje en la tabla de demostracion
    INSERT INTO demostracion_triggers(mensaje) VALUES ('SE INSERTO NUEVO REGISTRO');
    -- NEW > sera la informacion que me viene en el trigger, la informacion que se agregara ni bien se ejecute el trigger
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_registrar_registros
AFTER INSERT ON clientes
FOR EACH ROW -- Cada vez que se haga un nuevo ingreso de un cliente se ejecutara el trigger
EXECUTE FUNCTION registrar_accion();

INSERT INTO clientes (nombre, correo, status, activo) VALUES
('Jose Martines Perez', 'jmartines@gmail.com', 'BUEN CLIENTE', true);

-- 
CREATE OR REPLACE FUNCTION crear_clientes_y_cuentas(
    nombre_cliente TEXT,
    correo_cliente TEXT,
    status_cliente status_enum,
    cliente_activo BOOLEAN,
    tipo_moneda tipo_moneda_enum)
RETURNS VOID AS $$
-- Justo antes de empepzar la funcion tenemos que declarar las variables a utilizar en la funcion
DECLARE
    nuevo_cliente_id INT; -- Este cliente_id lo usare para el momento de crear la cuenta relacionarlo con el 
-- Inicial a ejecucion de la funcion
BEGIN
    -- RETURNING se puede llamar cuando hacemos un INSERRT | UPDATE | DELETE y sirve para retornar la informacion resultante de la operacion
    INSERT INTO clientes (nombre, correo, status, activo) VALUES (nombre_cliente, correo_cliente, status_cliente, cliente_activo) RETURNING id INTO nuevo_cliente_id;

    -- Ahora procedemos a crear la cuenta del cliente
    INSERT INTO cuentas (numero_cuenta, tipo_moneda, cliente_id) VALUES ('', tipo_moneda, nuevo_cliente_id);
END;
$$ LANGUAGE plpgsql;

-- Insertarmos un cliente
SELECT crear_clientes_y_cuentas('Shrek', 'shrek@dreamworks.com', 'BUEN CLIENTE', TRUE, 'DOLARES');

-- Para ver las funciones qwue existen en la BD
\df

BEGIN;
INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
(4, null, 100, NOW());

INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
(4, 3, 20, NOW());

INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
(null, 4, 40, NOW());

-- TODO ESTA BIEN Guardamos los cambios con de manera permanente
COMMIT;

-- SI LLEGASE A FALLAR ALGO PODEMOS DEJAR SIN EFECTO ESTE GRUPO DE OPERACION
ROLLBACK;