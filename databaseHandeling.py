__author__ = 'erlend'

import sys
import mysql.connector as mysql_conn
from mysql.connector import errorcode as mysql_error

#class variables

host_of_db = 'localhost'
user_log_in = 'root'
user_password = '***'
name_of_db = 'location_id'


def tryConnection(): ## tests the database connection

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

def sendLocationToDatabase(location):

    connection = tryConnection()
    cursor = connection.cursor()


    add_location = ("INSERT INTO assosiate_location_with_id" " (location,id,computer_status,program_status,time) "  "VALUES (%s,%s,%s,%s,%s)")
    data_location = (location, 'NULL', '0','0','0') #location has to be dynamic

    cursor.execute(add_location, data_location)
    connection.commit()

    cursor.close()
    connection.close()

def recieveIdFromDatabase(location):
    connection = tryConnection()
    cursor = connection.cursor()

    query = ("SELECT id FROM  `assosiate_location_with_id` WHERE  `location` =" + location)

    cursor.execute(query)

    result = cursor.fetchone()
    id = result[0]

    print(id)

    cursor.close()
    connection.close()

    return str(id)

def checkTime(id): #should only use resources when ping is lost

    connection = tryConnection()
    cursor = connection.cursor()

    query = ("SELECT time FROM  `assosiate_location_with_id` WHERE  `id` =" + id)

    cursor.execute(query)

    result = cursor.fetchone()

    outcome = str(result[0])

    return outcome

def checkComputerStatus(id): #should only use resources when ping is lost

    connection = tryConnection()
    cursor = connection.cursor()

    query = ("SELECT computer_status FROM  `assosiate_location_with_id` WHERE  `id` =" + id)

    cursor.execute(query)

    result = cursor.fetchone()

    outcome = str(result[0])

    if(outcome == '0'):
        return False

    else:
        return True

def checkProgramStatus(id): #should only use resources when ping is lost

    connection = tryConnection()
    cursor = connection.cursor()

    query = ("SELECT program_status FROM  `assosiate_location_with_id` WHERE  `id` =" + id)

    cursor.execute(query)

    result = cursor.fetchone()

    outcome = str(result[0])

    if(outcome == '0'):
        return False

    else:
        return True

def updateTime(location, time):

    connection = tryConnection()
    cursor = connection.cursor()


    insert_new_bool = ("UPDATE assosiate_location_with_id SET time = %s WHERE id = %s ")
    data_location = (time,location) #location has to be dynamic

    cursor.execute(insert_new_bool, data_location)
    connection.commit()

    cursor.close()
    connection.close()

def updateComputerStatus(location, value):

    connection = tryConnection()
    cursor = connection.cursor()


    insert_new_bool = ("UPDATE assosiate_location_with_id SET computer_status = %s WHERE id = %s ")
    data_location = (value,location) #location has to be dynamic

    cursor.execute(insert_new_bool, data_location)
    connection.commit()

    cursor.close()
    connection.close()

def updateProgramStatus(location, value):

    connection = tryConnection()
    cursor = connection.cursor()


    insert_new_bool = ("UPDATE assosiate_location_with_id SET program_status = %s WHERE id = %s ")
    data_location = (value,location) #location has to be dynamic

    cursor.execute(insert_new_bool, data_location)
    connection.commit()

    cursor.close()
    connection.close()


def getLocationName(id):

    connection = tryConnection()
    cursor = connection.cursor()

    query = ("SELECT location FROM  `assosiate_location_with_id` WHERE  `id` =" + id)

    cursor.execute(query)

    result = cursor.fetchone()

    outcome = str(result[0])

    return outcome

def setTimeOfDeath(location,time):

    connection = tryConnection()
    cursor = connection.cursor()


    insert_new_bool = ("UPDATE assosiate_location_with_id SET timeofdeath = %s WHERE id = %s ")
    data_location = (time,location) #location has to be dynamic

    cursor.execute(insert_new_bool, data_location)
    connection.commit()

    cursor.close()
    connection.close()

def getTimeOfDeath(id):

    connection = tryConnection()
    cursor = connection.cursor()

    query = ("SELECT timeofdeath FROM  `assosiate_location_with_id` WHERE  `id` =" + id)

    cursor.execute(query)

    result = cursor.fetchone()

    outcome = str(result[0])

    return outcome