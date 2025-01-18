/*
  Warnings:

  - A unique constraint covering the columns `[nombre]` on the table `Equipo` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "Equipo_nombre_key" ON "Equipo"("nombre");
