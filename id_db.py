__author__ = 'erlend'

import sys
import mysql.connector as mysql_conn
from mysql.connector import errorcode as mysql_error

#class variables

host_of_db = 'localhost'
user_log_in = 'root'
user_password = '****'
name_of_db = 'location_id'





def try_connection():

    try:
        connection = mysql_conn.connect(user=user_log_in,password=user_password,host=host_of_db,database=name_of_db)
        return connection
    except mysql_conn.Error as err:
        if err.errno == mysql_error.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql_error.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    else:
        connection.close()


def send_to_id_db(location):

    connection = try_connection()
    cursor = connection.cursor()


    add_location = ("INSERT INTO assosiate_location_with_id" " (location,id) "  "VALUES (%s,%s)")
    data_location = (location, 'NULL') #location has to be dynamic

    cursor.execute(add_location, data_location)
    connection.commit()

    cursor.close()
    connection.close()

def recieve_id_from_db():
    connection = try_connection()
    cursor = connection.cursor()

    query = ("SELECT COUNT(*) FROM assosiate_location_with_id")

    cursor.execute(query)

    result = cursor.fetchone()
    id = result[0]

    print(id)

    cursor.close()
    connection.close()

    return str(id)