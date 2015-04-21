import string
__author__ = 'erlend'
from time import sleep as zzz
import socket


server_ip = '178.62.12.142'
server_port = 5000


def setLocation():

    while True:
        location = input('Where is this recorder located?')
        confirmation = input('Please confirm')

        if(str.upper(location) == str.upper(confirmation)):
            if(str.upper(input('is the location ' + location + " correct? Y/N")) == 'Y'):
                break
            else:
                continue

        print('\nPlease make sure your first and second input matches')

    return location

def getLocalIp():

    computer_name = socket.gethostname()

    all_info = (socket.gethostbyname_ex(computer_name))
    list_of_ip = all_info[2]

    if(len(list_of_ip)>=2):
        ip = list_of_ip[1]
    else:
        ip = list_of_ip[0]


    return ip

def tellServerYouAreUp():

    location = setLocation()
    ip_host_of_client = getLocalIp()
    port_to_try = 5000 #will be auto assigned if occupied by another system

    server = (server_ip, server_port) #ip of server

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_host_of_client,port_to_try))

    while True:
        message = str.encode(location)
        s.sendto(message,server)
        print('Local ip is: ' + ip_host_of_client)
        zzz(3)

    s.close()

def Main():

    tellServerYouAreUp()


if __name__ == '__main__':
    Main()