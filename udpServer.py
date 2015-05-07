__author__ = 'erlend'

import socket
import databaseHandeling as dbh
import statusMonitor
from threading import Thread
import datetime

#variables for server
host = '178.62.12.142'
port = 5000


def welcomeMessage(): ## prints welcome message
    print ("\n\n\nWelcome to <SYSTEM MONITOR> <v1.0.0>\n\n\n")

def bindSocket(): ## binds socket to host and port of the digital ocean server

    local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_socket.bind((host,port))

    return local_socket

def getCurrentTime(): ## Finds the current system time on the server

        time_now = datetime.datetime.now()
        time_now = (time_now.strftime('%S')) ## skal oppdateres til %H%M%S

        return time_now

def recieveDataFromClient(localsocket): ## Listens for info from recorders

    while True:

        data, addr = localsocket.recvfrom(1024)
        data = bytes.decode(data)

        to_check = data.split(',')

        location_id = to_check[0]
        first_itteration = to_check[1]
        task_status = to_check[2]

        if(task_status == '1'):
            dbh.updateProgramStatus(location_id,'1')

        elif(task_status == '0'):
            dbh.updateProgramStatus(location_id,'0')


        if(first_itteration == '0'):
            dbh.sendLocationToDatabase(location_id)
            location_id = dbh.recieveIdFromDatabase(location_id)

            print('\n' + location_id + " was accepted to the database\n")
            dbh.setTimeOfDeath(location_id,statusMonitor.setTimeOfDeath())
            localsocket.sendto(str.encode(location_id),addr)

            dbh.updateTime(location_id,getCurrentTime())

        else:

            try:
                isActive = dbh.checkComputerStatus(location_id)
            except Exception as e:
                isActive = False

            if not isActive:

                dbh.updateComputerStatus(location_id,'1')
                dbh.updateTime(location_id,getCurrentTime())

                t = Thread(target=statusMonitor.confirmStatus,args=(location_id))
                t.start()

            if isActive:

                dbh.updateTime(location_id,getCurrentTime())


    localsocket.close()


def Main():

    welcomeMessage()
    recieveDataFromClient(bindSocket())


if __name__ == '__main__':
    Main()





