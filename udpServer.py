__author__ = 'erlend'

import socket
import id_db as id_database

#variables for server
host = '178.62.12.142'
port = 5000


def bind_socket():

    print ("starter bind socket")
    local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ("socket.socket")
    local_socket.bind((host,port))
    print ("bind")
    recieve_data_from_client(local_socket)

def recieve_data_from_client(local_socket):

    print ("server has started")

    while True:

        data, addr = local_socket.recvfrom(1024)
        data = bytes.decode(data)

        to_check = data.split(',')

        location_id = to_check[0]
        is_true = to_check[1]


        if(is_true == '0'):
            id_database.send_to_id_db(location)
            location_id = id_database.recieve_id_from_db()
            print('\n' + location_id + " was accepted to the database\n")
            local_socket.sendto(str.encode(location_id),addr)

        else:
            id_database.check_status(location_id)
            print(location_id + " is active at public ip " + str(addr))



    local_socket.close()

def pass_data_to_id_db(data):

    id_database.try_connection(data)

def Main():

    bind_socket()

if __name__ == '__main__':
    Main()





