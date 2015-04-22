__author__ = 'erlend'

from time import sleep as zzz
import udpServer
import id_db
import datetime



def confirm_status(id):

    while True:

        current_system_time = datetime.datetime.now()
        current_system_time = (current_system_time.strftime('%H%M'))

        last_ping_time = id_db.check_time(id)

        result = int(current_system_time) - int(last_ping_time)

        print('Time scince last ping from ' + id + ' is ' + str(result) + ' minute(s)')

        if(result>=1):
            zzz(3)
            print(current_system_time)
            zzz(3)
            print('\n' + last_ping_time)
            zzz(3)
            print('breaking while')

            break

        zzz(5)

        print('thread for id: ' + id + ' is still running')

    print('Client ' + id + ' is down!')
    id_db.update__status(id,'0')



