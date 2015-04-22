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

        if(result < 0): # when system time is 1 and last ping is 59
            result = 1

        print('Time scince last ping from ' + id + ' is ' + str(result) + ' second(s)')

        if(result>=10):
            print('breaking while')

            break

        zzz(1)

    print('CLIENT WITH ' + id + ' IS DOWN!')
    id_db.update__status(id,'0')



