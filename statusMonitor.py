__author__ = 'erlend'

from time import sleep as zzz
import udpServer
import databaseHandeling as dbh
import mailOnFail


def confirmStatus(id):

    control_variable = 300
    isSent = False

    mailOnFail.mailOnFail(id,' is UP!')

    while True:

        current_system_time = udpServer.getCurrentTime()

        last_ping_time = dbh.checkTime(id)

        result = int(current_system_time) - int(last_ping_time)

        control_variable = last_ping_time

        programstatus = dbh.checkProgramStatus(id)

        if(programstatus == False and isSent == False):
            mailOnFail.mailOnFail(id,' is not recording!')
            isSent = True

        if(programstatus == True and isSent == True):
            mailOnFail.mailOnFail(id,' is now recording again!')

        print('Time scince last ping from ' + id + ' is ' + str(result) + ' second(s)')

        if(result >= 10):
            break

        if(result<0 and (last_ping_time == control_variable)): #handles the situation where result is stuck at >0
            zzz(4)
            if((dbh.checkTime(id)) == control_variable):
                break

        zzz(5)


    print('CLIENT WITH ID: ' + id + ' IS DOWN!')
    dbh.updateComputerStatus(id,'0')
    dbh.updateProgramStatus(id,'0')
    mailOnFail.mailOnFail(id, ' is DOWN!')
    return



