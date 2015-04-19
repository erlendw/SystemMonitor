__author__ = 'erlend'

import socket

def Main():
    host = '178.62.12.142'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print ("server has started")
    while True:
        data, addr = s.recvfrom(1024)

        data = bytes.decode(data)

        if(countDown(data)):
            print(data + " is active at public ip " + str(addr))
        else:
            continue





    s.close()


def countDown(recieved):
    return True


if __name__ == '__main__':
    Main()





