__author__ = 'erlend'

from time import sleep as zzz
import udpServer
import id_db
import datetime



def confirm_status(id):

    while True:

        current_system_time = udpServer.getCurrentTime()

        last_ping_time = id_db.check_time(id)

        result = int(current_system_time) - int(last_ping_time)

        print('Time scince last ping from ' + id + ' is ' + str(result) + ' second(s)')

        if(result >= 10):
            break

        zzz(1)

    print('CLIENT WITH ID: ' + id + ' IS DOWN!')
    id_db.update__status(id,'0')
    id_db.update__status__program(id,'0')



