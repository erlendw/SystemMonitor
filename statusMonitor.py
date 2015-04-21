__author__ = 'erlend'

from time import sleep as zzz
import udpServer
import id_db


def confirm_status(id):
    zzz(3) #has to be greater than ping rate
    #if(statuschange)

    print('vi kom hit!')

    counter = 0

    while True:
        print('Im worth while')
        zzz(4)
        if(id == ):
            print('we have a new ping!')
            break
        counter += 1

    if(counter>100):
        print('the ping is gone, update database')
        id_db.update_status_of_location(id, '0')
    #i was pinged with this number
    #now i expect the same number within 5 seconds