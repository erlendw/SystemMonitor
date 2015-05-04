import string
__author__ = 'erlend'
from time import sleep as zzz
import socket
import pickle
import subprocess
import re

server_ip = '178.62.12.142'
server_port = 5000

def giveId():

    while True:
        location = input('Where is this recorder located? ')
        confirmation = input('Retype location ' + location + ' to confirm: ')

        if(str.upper(location) == str.upper(confirmation)):
            if(str.upper(input('is the location ' + str.upper(location) + ' correct? Y/N ')) == 'Y'):
                break
            else:
                print('\nRestarting input procedure\n')
                zzz(0.3)
                print('.')
                zzz(0.3)
                print('.')
                zzz(0.3)
                print('.\n')
                continue

        print('\n************Please make sure your first and second input matches************\n')
        zzz(0.3)
        print('.')
        zzz(0.3)
        print('.')
        zzz(0.3)
        print('.\n')

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

def testIp():

    current_ip = getLocalIp()

    try:

        old_ip = pickle.load(open('ip.p','rb'))

    except Exception as e:

        old_ip = ''


    if(old_ip != current_ip):

        pickle.dump(current_ip,open('ip.p', 'wb'))
        return True

    elif(old_ip == current_ip):

        return False

def findRunningProcesses():

    processList = []

    cmd = 'WMIC PROCESS get Caption'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    for line in proc.stdout:
        line = bytes.decode(line)
        line = re.sub(r'\s+', '', line)
        processList.append(line)

    return processList

def testForProcess():

    processList = findRunningProcesses()

    for i in range(len(processList)):
        if(processList[i] == 'ManagementApplication.exe'): #process is hardcoded for now
            return True

    return False

def sendInfoToServer():

    first_itteration = testIp()

    ip_host_of_client = getLocalIp()
    port_to_try = 5000 #will be auto assigned if occupied by another system

    server = (server_ip, server_port) #ip of server

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_host_of_client,port_to_try))

    if(first_itteration):

        location_id = giveId()
        put_in_db = '0'

    if not (first_itteration):

        location_id = pickle.load(open('id.p','rb'))
        put_in_db = '1'

    while True:

        program_is_running = testForProcess()

        if(program_is_running):
            isRunning = '1'

        if not(program_is_running):
            isRunning = '0'

        message = str.encode(location_id + ',' + put_in_db + ',' + isRunning)

        print(message)

        s.sendto(message,server)

        print('*ping*')

        if(first_itteration):
            put_in_db = '1' #Tells server not to ubdate db
            first_itteration = False #we are no longer on first itteration

            location_id, addr = s.recvfrom(1024)
            location_id = bytes.decode(location_id)

            pickle.dump(location_id,open('id.p', 'wb'))
            print('server svarte med id: ' + location_id)



        zzz(3)

    s.close()

def Main():

    findRunningProcesses()
    sendInfoToServer()


if __name__ == '__main__':
    Main()