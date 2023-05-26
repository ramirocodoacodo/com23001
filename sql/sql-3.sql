USE world;

/*
12. Listar todos los datos de los países cuya expectativa de vida 
supere los setenta y cinco años, ordenados bajo este concepto 
de forma ascendente. (Se esperan 15 columnas y 62 registros).
*/
-- Operadores
SELECT * 
FROM country
WHERE LifeExpectancy > 75
ORDER BY LifeExpectancy ASC
;

-- SELECT Name AS Pais, Continent, LifeExpectancy AS EDV
SELECT UPPER(TRIM(Name)) AS Pais, Continent, LifeExpectancy AS EDV  -- Con funciones escalares (de cadena)
FROM country
WHERE LifeExpectancy > 75
	AND (Continent LIKE 'South America'
    OR Continent LIKE 'Oceania')
    AND Name LIKE '%A%'
ORDER BY LifeExpectancy ASC
;

/*
17. Listar todos los datos de los países situados en Europa, 
Asia o Sudamérica. (Se esperan 15 columnas y 111 registros).
*/
-- IN / NOT / Sub-consultas
SELECT * 
FROM country
-- WHERE Continent NOT IN ('South America', 'Europe', 'Asia')
WHERE Continent IN (SELECT DISTINCT Continent
					FROM country
					WHERE Continent LIKE 'A%')  -- EXISTS (alternativa)
;

-- DISTINCT 
-- Mostrar todos los continentes que empiecen con A
SELECT DISTINCT Continent
FROM country
WHERE Continent LIKE 'A%';

/*
20. Listar todos los datos de las ciudades de entre 125 mil y 130 mil habitantes. 
(Se esperan 5 columnas y 138 registros).
*/
-- BETWEEN
SELECT *
FROM city
-- WHERE Population >= 125000 AND Population <= 130000
WHERE Population BETWEEN 125000 AND 130000  -- Formas equivalentes
;

/*
26. Listar los nombres de los países sudamericanos junto a los nombres 
(alias 'Capital') de sus capitales. (Se esperan 2 columnas y 14 registros).
*/
-- JOIN (WHERE)
SELECT country.Name AS Pais, Capital, city.ID, city.Name
FROM country, city
WHERE Continent LIKE 'South America'
	AND Capital = city.ID;

-- JOIN (INNER JOIN)
SELECT country.Name AS Pais, -- Capital, city.ID, 
	city.Name
FROM country
	INNER JOIN city ON Capital = city.ID
WHERE Continent LIKE 'South America'
;

-- LEFT JOIN
-- Qué países NO tienen ciudades cargadas en la tabla city*
SELECT CountryCode
FROM city; -- 4079 ciudades

SELECT CountryCode
FROM city; -- 4079 ciudades

SELECT DISTINCT CountryCode
FROM city; -- 232 países en la tabla ciudades

SELECT COUNT(*)
FROM city; -- 4079

SELECT Name
FROM country;  -- 239 países

SELECT co.Name AS Pais, -- Capital, city.ID, 
	city.Name
FROM country co
	-- INNER JOIN city ON Capital = city.ID
	-- LEFT JOIN city ON Capital = city.ID
	LEFT JOIN city ON co.Code = city.CountryCode
WHERE city.Name IS NULL
;

-- Funciones de agregación, GROUP BY, HAVING, Funciones escalares
SELECT COUNT(*)
FROM city; -- 4079

SELECT SUM(Population) AS 'Población Total'
FROM country
;

/*
42. Mostrar las diez regiones de mayor expectativa de vida promedio. 
(Se esperan 2 columnas y 10 registros).
HAVING: EDV (Promedio) > 75

*/
-- Orden de las cláusulas*
SELECT Region, AVG(LifeExpectancy) AS EDVP
FROM country
-- WHERE LifeExpectancy > 75  -- MAL!
-- JOIN ... ON
GROUP BY Region
HAVING AVG(LifeExpectancy)>75
ORDER BY AVG(LifeExpectancy) DESC
LIMIT 10; -- 25 REGIONES
-- 'Caribbean', '77.01818' (WHERE: solo de los paises cuya exp. de vida es mayor 75)
-- 'Caribbean', '73.05833'
-- 'Eastern Asia', '75.25000'

-- Crear una vista*
CREATE VIEW reporte_EDVP AS
SELECT Region, COUNT(*) AS cant, AVG(LifeExpectancy) AS EDVP
FROM country
-- JOIN ON
-- WHERE LifeExpectancy > 75  -- MAL!
GROUP BY Region
HAVING AVG(LifeExpectancy) > 75
ORDER BY AVG(LifeExpectancy) DESC
LIMIT 10;

SELECT * FROM reporte_EDVP;
-- SoloLearn: MySQL
-- Back-up
