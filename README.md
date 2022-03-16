# global-temps-rest-api
REST API for accessing historical global temperature data using the dataset provided on data.world:

https://data.world/data-society/global-climate-change-data

## Setup

The following describes how to setup the REST API on your local PC for testing / development purposes.

Prerequisites:

- [Python 3.9.1](https://www.python.org/downloads/release/python-391/)
- [MS SQL Server instance - developer edition](https://www.microsoft.com/en-au/sql-server/sql-server-downloads)

### Database setup

1. Connect to the MS SQL Server instance and run:

    ```tsql
    CREATE DATABASE global_temperatures
    ```
   
2. Execute the SQL file [create_tables.sql](sql/create_tables.sql) to create the tables required for the API.
3. Edit the SQL file [insert_csv_data.sql](sql/insert_csv_data.sql) to point to the location of 
[global_temperatures.csv](csv/global_temperatures.csv) on your local PC.
4. Execute [insert_csv_data.sql](sql/insert_csv_data.sql) to insert data from the CSV to the database.
