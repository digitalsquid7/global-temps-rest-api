USE global_temperatures

IF OBJECT_ID('dbo.daily_average_temperature', 'U') IS NOT NULL
   DROP TABLE daily_average_temperature

IF OBJECT_ID('dbo.city', 'U') IS NOT NULL
   DROP TABLE city

IF OBJECT_ID('dbo.country', 'U') IS NOT NULL
   DROP TABLE country

CREATE TABLE country
(
    id INT IDENTITY(1,1),
    country_name NVARCHAR(1000) NOT NULL,
    CONSTRAINT pk__country PRIMARY KEY (id)
)

CREATE TABLE city
(
    id INT IDENTITY(1,1),
    country_id INT NOT NULL,
    city_name NVARCHAR(1000) NOT NULL,
    latitude DECIMAL(5, 2) NOT NULL,
    longitude DECIMAL(5, 2) NOT NULL,
    CONSTRAINT pk__city PRIMARY KEY (id),
    CONSTRAINT fk__city__country FOREIGN KEY (country_id) REFERENCES country(id)
)

CREATE TABLE daily_average_temperature
(
    id INT IDENTITY(1,1),
    city_id INT NOT NULL,
    temperature_recorded_date DATE NOT NULL,
    average_temperature DECIMAL(5, 3) NOT NULL,
    average_temperature_uncertainty DECIMAL(5, 3) NOT NULL,
    CONSTRAINT pk__daily_average_temperature PRIMARY KEY (id),
    CONSTRAINT fk__daily_average_temperature__city FOREIGN KEY (city_id) REFERENCES city(id)
)

CREATE UNIQUE INDEX uq__country__country_name ON country (country_name)
CREATE UNIQUE INDEX uq__city__city_name ON city (city_name)
CREATE INDEX ix__city__country_id ON city (country_id)
CREATE INDEX ix__daily_average_temperature__city_id ON daily_average_temperature (city_id)
CREATE INDEX ix__daily_average_temperature__average_temperature ON daily_average_temperature (average_temperature)
