__author__ = 'erlend'

from time import sleep as zzz
import udpServer
import id_db
import mailOnFail


def confirm_status(id):

    control_variable = 300
    isSent = False



    while True:

        current_system_time = udpServer.getCurrentTime()

        last_ping_time = id_db.check_time(id)

        result = int(current_system_time) - int(last_ping_time)

        control_variable = last_ping_time

        programstatus = id_db.check_program_status(id)

        if(programstatus == False and isSent == False):
            mailOnFail.mailOnFail(id,' is not recording!')
            isSent = True

        if(programstatus == True):
            isSent = False

        print('Time scince last ping from ' + id + ' is ' + str(result) + ' second(s)')

        if(result >= 10):
            break

        if(result<0 and (last_ping_time == control_variable)): #handles the situation where result is stuck at >0
            zzz(4)
            if((id_db.check_time(id)) == control_variable):
                break

        zzz(5)


    print('CLIENT WITH ID: ' + id + ' IS DOWN!')
    id_db.update__status(id,'0')
    id_db.update__status__program(id,'0')
    mailOnFail.mailOnFail(id, 'DOWN!')
    return



