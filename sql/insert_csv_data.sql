CREATE TABLE #csv_daily_average_temperature
(
    temperature_recorded_date NVARCHAR(1000),
    average_temperature DECIMAL(5, 3),
    average_temperature_uncertainty DECIMAL(5, 3),
    city_name NVARCHAR(1000),
    country_name NVARCHAR(1000),
    latitude NVARCHAR(1000),
    longitude NVARCHAR(1000),
)

BULK INSERT #csv_daily_average_temperature
FROM 'path\to\global_temperatures.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR='\n'
);

INSERT INTO country (country_name)
SELECT country_name
FROM #csv_daily_average_temperature
GROUP BY country_name

INSERT INTO city (country_id, city_name, longitude, latitude)
SELECT
    country.id,
    city_name,
    CONVERT(DECIMAL(5,2), LEFT(longitude, LEN(longitude)-1)) longitude,
    CONVERT(DECIMAL(5,2), LEFT(latitude, LEN(latitude)-1)) latitude
FROM
(
    SELECT city_name, country_name, longitude, latitude
    FROM #csv_daily_average_temperature
    GROUP BY city_name, country_name, longitude, latitude
 ) unq_cities
JOIN country on country.country_name = unq_cities.country_name

INSERT INTO daily_average_temperature (city_id, temperature_recorded_date, average_temperature, average_temperature_uncertainty)
SELECT
    city.id,
    CAST(temperature_recorded_date AS DATE),
    CAST(average_temperature AS DECIMAL(5,3)),
    CAST(average_temperature_uncertainty AS DECIMAL(5,3))
FROM #csv_daily_average_temperature
JOIN city ON city.city_name = #csv_daily_average_temperature.city_name
WHERE
    #csv_daily_average_temperature.average_temperature IS NOT NULL
    AND #csv_daily_average_temperature.average_temperature_uncertainty IS NOT NULL

DROP TABLE #csv_daily_average_temperature
