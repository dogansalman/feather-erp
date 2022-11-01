import util
from gc import callbacks
import psycopg2
from psycopg2 import sql
import logging

username = util.get_config("DATABASE", "USERNAME")
user_password = util.get_config("DATABASE", "PASSWORD")
host = util.get_config("DATABASE", "HOST")
port = util.get_config("DATABASE", "PORT")
db = util.get_config("DATABASE", "DB")

psql_connection_string = f"host={host} port={port} dbname=postgres user={username}  password={user_password}"
connection = None
cursor = None

try:
    connection = psycopg2.connect(psql_connection_string)
    connection.autocommit = True

    print(f"Connected with connection string {psql_connection_string}")
    cursor = connection.cursor()
    cursor.execute(sql.SQL('CREATE DATABASE {};').format(sql.Identifier(db)))
    print("created database")


except (Exception) as error:
    print("Error while connecting to PostgreSQL", error)
    logging.error(error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
