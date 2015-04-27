__author__ = 'erlend'

import socket
import id_db as id_database
import statusMonitor
from threading import Thread
import datetime

#variables for server
host = '178.62.12.142'
port = 5000
import mailOnFail

def welcomeMessage():
    print ("\n\n\nWelcome to <SYSTEM MONITOR> <v1.0.0>\n\n\n")

def bind_socket():

    local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_socket.bind((host,port))

    return local_socket

def getCurrentTime():

        time_now = datetime.datetime.now()
        time_now = (time_now.strftime('%S'))

        return time_now

def recieve_data_from_client(local_socket):

    isSent = False

    while True:

        data, addr = local_socket.recvfrom(1024)
        data = bytes.decode(data)

        to_check = data.split(',')

        location_id = to_check[0]
        first_itteration = to_check[1]
        task_status = to_check[2]

        if(task_status == '1'):
            id_database.update__status__program(location_id,'1')
            isSent = False
        elif(task_status == '0'):
            id_database.update__status__program(location_id,'0')

            if not(isSent):
                mailOnFail.mailOnFail(location_id, 'not recording!')
                isSent = True

        if(first_itteration == '0'):
            id_database.send_id_to_id_db(location_id)
            location_id = id_database.recieve_id_from_db()

            print('\n' + location_id + " was accepted to the database\n")
            local_socket.sendto(str.encode(location_id),addr)

            id_database.update__time(location_id,getCurrentTime())

        else:

            isActive = id_database.check_computer_status(location_id)

            if not isActive:

                id_database.update__status(location_id,'1')
                id_database.update__time(location_id,getCurrentTime())

                t = Thread(target=statusMonitor.confirm_status,args=(location_id))
                t.start()

            if isActive:

                id_database.update__time(location_id,getCurrentTime())


    local_socket.close()

def pass_data_to_id_db(data):

    id_database.try_connection(data)


def Main():

    welcomeMessage()
    recieve_data_from_client(bind_socket())


if __name__ == '__main__':
    Main()





