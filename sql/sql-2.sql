-- SENTENCIAS DDL

-- Creo el esquema
CREATE SCHEMA `escuela` DEFAULT CHARACTER SET utf8 ;
-- DROP SCHEMA IF EXISTS escuela;

-- Selecciono el esquema
USE escuela;

-- Creo una tabla
CREATE TABLE alumnos (
  `id_alumno` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `apellido` VARCHAR(100) NULL,
  fecha_nacimiento DATE,
  PRIMARY KEY (`id_alumno`));

CREATE TABLE `materias` (
  `id_materia` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NULL,
  `fecha_creacion` datetime NULL,
  PRIMARY KEY (`id_materia`)
);

-- Eliminar una tabla
-- DROP TABLE IF EXISTS materias;

-- Modificar una tabla
ALTER TABLE `materias` 
CHANGE COLUMN `nombre` `materia` VARCHAR(100) NULL DEFAULT NULL ;

ALTER TABLE `alumnos` 
ADD COLUMN `email` VARCHAR(100) NULL DEFAULT NULL ;

ALTER TABLE `alumnos` 
DROP COLUMN `email`;

-- Sentencias DML

-- CRUD: Crear, Modificar, Eliminar, Leer registros
-- Consulto (Leer) todos los registros de la tabla alumnos
SELECT *
FROM alumnos;

-- Agregar
INSERT INTO alumnos (nombre, apellido, fecha_nacimiento) 
VALUES ('Juan', 'Sánchez', '19900101');
INSERT INTO alumnos (id_alumno, nombre, apellido) 
VALUES (1000, 'Juan', 'Pérez');
INSERT INTO alumnos (nombre, apellido) 
VALUES ('Juan', 'Gómez');

SELECT *
FROM materias;

INSERT INTO materias (materia, fecha_creacion) 
VALUES ('Matemáticas', NULL);
-- INSERT INTO materias
-- VALUES (2, 'Historia', NULL);  -- Mala práctica. Siempre incluir los campos a agregar
INSERT INTO materias (materia, fecha_creacion) 
VALUES ('Historia', NOW());

-- Vaciar tablas
-- TRUNCATE TABLE materias;

-- Modificar
UPDATE materias
SET materia = 'Matemática'
WHERE id_materia = 1;

UPDATE materias
SET materia = 'Matemática', 
fecha_creacion = NOW()
WHERE id_materia = 1;

-- Actualizando todos registros
UPDATE materias
SET fecha_creacion = NOW()
;

-- Eliminar registros
DELETE FROM alumnos;  -- OJO! Usar siempre WHERE
DELETE FROM alumnos WHERE id_alumno = 1000;
SELECT * FROM alumnos WHERE id_alumno = 1004;
-- DELETE FROM alumnos WHERE id_alumno = 1004;

-- world.sql
-- Guía práctica de SQL.pdf

/*
5. Listar el nombre, la cantidad de habitantes, la superficie y 
una columna llamada 'Densidad' con el resultado de la densidad 
poblacional de todos los países. 
(Se esperan 4 columnas y 239 registros).
*/
SELECT
    `Name`,
    Population,
    SurfaceArea,
    Population / SurfaceArea AS `Densidad Poblacional`
FROM
    country;

/*
10. Listar nombre y continente de los cien países con mayor 
expectativa de vida. Si hubiera países que tengan la misma 
expectativa de vida, mostrar primero a los de menor superficie. 
(Se esperan 2 columnas y 100 registros).
*/
SELECT
    `Name`,
    Continent -- ,
--    LifeExpectancy,
--    SurfaceArea
FROM
    country
ORDER BY LifeExpectancy DESC, 
SurfaceArea
LIMIT 100;

-- TO-DO:
-- Back-up
