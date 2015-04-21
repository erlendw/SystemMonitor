__author__ = 'erlend'

import socket
import id_db as id_database
import statusMonitor
from threading import Thread

#variables for server
host = '178.62.12.142'
port = 5000

def bind_socket():

    local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_socket.bind((host,port))
    recieve_data_from_client(local_socket)

def recieve_data_from_client(local_socket):

    print ("\n\n\nserver has started\n\n\n")

    while True:

        data, addr = local_socket.recvfrom(1024)
        data = bytes.decode(data)

        to_check = data.split(',')

        location_id = to_check[0]
        is_true = to_check[1]


        if(is_true == '0'):
            id_database.send_to_id_db(location_id)
            location_id = id_database.recieve_id_from_db()
            print('\n' + location_id + " was accepted to the database\n")
            local_socket.sendto(str.encode(location_id),addr)

        else:

            isActive = id_database.check_status(location_id)

            if not isActive and location_id != '0':

                print('activity from location: ' + location_id)
                print('need for new thread')
                t = Thread(target=statusMonitor.confirm_status,args=(location_id))
                t.start()

        l







    local_socket.close()

def pass_data_to_id_db(data):

    id_database.try_connection(data)


def Main():

    bind_socket()

if __name__ == '__main__':
    Main()





