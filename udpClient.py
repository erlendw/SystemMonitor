import string
__author__ = 'erlend'
from time import sleep as zzz

import socket

def Main():

    location = input('Where is this recorder located?')

    computer_name = socket.gethostname()

    all_info = (socket.gethostbyname_ex(computer_name))
    list_of_ip = all_info[2]

    if(len(list_of_ip)>=2):
        ip = list_of_ip[1]
    else:
        ip = list_of_ip[0]

#    for i in range(0, len(list_of_ip)):
#       if(list_of_ip[i].startswith('192')):
#            ip = list_of_ip[i]
#            break

    host = ip
    port = 5000




    server = ('178.62.12.142', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    while True:
        message = str.encode(location)
        s.sendto(message,server)
        print('Local ip is: ' + host)
        zzz(3)

    s.close()

if __name__ == '__main__':
    Main()