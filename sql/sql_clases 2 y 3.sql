USE world;  -- LA BD con la que voy a trabajar

/*
Los datos de paises cuya poblacion se encuentra 
entre 1.000.000 y 300 millones, solo muestro Arg., Brazil, Aus. Ordenado de forma DESC. 
y muestro los primeros 10 regitros.
*/
SELECT 
    NAME AS Pais,
    `Population`,
    `SurfaceArea`,
    ROUND(`Population` / `SurfaceArea`) AS 'Densidad Poblacional'
FROM
    `country`
WHERE
    Population >= 1000000
        AND Population <= 300000000
        AND NAME IN ('Brazil' , 'Argentina', 'Australia')
ORDER BY `country`.`SurfaceArea` DESC
LIMIT 10;

-- Países cuya espectativa de vida es NULL
SELECT * 
FROM world.country
WHERE LifeExpectancy IS NOT NULL
;

-- Eliminando todas las ciudades de Australia
-- DELETE FROM country WHERE Code = 'AUS';
SELECT * FROM country WHERE Code = 'AUS';

-- DELETE FROM city WHERE CountryCode = 'AUS';
SELECT * FROM city WHERE CountryCode = 'AUS';

-- Ver todas las ciudades de Arg. (Campos: nombre, codigo, nombre de la ciudad, población)
SELECT country.Name, Code, city.Name, city.Population
FROM country
-- INNER JOIN city ON country.Code = city.CountryCode
LEFT JOIN city ON country.Code = city.CountryCode  -- Incluyo a Australia en mi reporte
WHERE country.Name IN ('Brazil' , 'Argentina', 'Australia')
;

-- contar ciudades por país
-- SELECT DISTINCT country.Name  -- MUESTRO VALORES DISTINTOS
SELECT country.Name, COUNT(ID)
FROM country
LEFT JOIN city ON country.Code = city.CountryCode
WHERE country.Name IN ('Brazil' , 'Argentina', 'Australia')
GROUP BY country.Name
;

-- Paises DE LATINOAMERICA con más de 100 ciudades cargadas 
SELECT country.Name, Region, COUNT(ID) AS cantidad
FROM country
INNER JOIN city ON country.Code = city.CountryCode
-- WHERE Region LIKE 'South America'
GROUP BY country.Name
HAVING Region LIKE 'South America' AND COUNT(ID) > 100
ORDER BY cantidad DESC
;

-- Paises cuya ciudad con mayor poblacion sea de más de 5.000.000 de hab.
SELECT country.Name, city.Name, city.Population  -- , COUNT(ID) AS cantidad
FROM country
INNER JOIN city ON country.Code = city.CountryCode
-- GROUP BY country.Name
-- HAVING COUNT(ID) > 100
WHERE city.Population > 5000000
-- ORDER BY cantidad DESC
;

SELECT country.Name, 
	-- city.Name, 
	MAX(city.Population)
FROM country
INNER JOIN city ON country.Code = city.CountryCode
GROUP BY country.Name
HAVING MAX(city.Population) > 5000000
;
