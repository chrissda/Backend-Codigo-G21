import express from "express";
import { usuarioEnrutador } from "./routes/usuario.routes.js";
import { equipoEnrutador } from "./routes/equipo.routes.js";
import { ZodError } from "zod";
import { Prisma } from "@prisma/client";
import cors from "cors";

const servidor = express()
servidor.use(express.json());

// CORS 
servidor.use(cors({ origi: ["http://127.0.0.1:5500"]}));

// Agregamos las rutas de nuestros enrutadores
servidor.use(usuarioEnrutador)
servidor.use(equipoEnrutador)

servidor.use((error, req, res, next) => {
    // Aca manejaremos los errores que podamos tener en toda nuestra aplicacion
    // Para manejar el error global se tiene que declarar LUEGO de todas las rutas sino evitara que ingrese al controlador adecuado
    if(error instanceof ZodError){
        return res.status(400).json({
            message: "Error al recibir la informacion",
            content: error.errors,
        });
    }
    // La clase PrismaClientKnowRequestError tiene la propiedad meta en la cual almacena el modelo que emitio el error al no econtrar la coincidencia en la bd
    if (error instanceof Prisma.PrismaClientKnownRequestError) {
        return res.status(404).json({
            message: `El ${error.meta.modelName} no existe`,
        });
    }

    return res.status(400).json({
        message: "Error al hacer la peticion",
    });
});

servidor.listen(process.env.PORT, () =>{
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
    );
});