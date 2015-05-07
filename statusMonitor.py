__author__ = 'erlend'

from time import sleep as zzz
import udpServer
import databaseHandeling as dbh
import mailOnFail
import datetime

def setTimeOfDeath(): #different formatting from method in udpServerm, finds exact time of death

        time_now = datetime.datetime.now()
        time_now = (time_now.strftime('%d%m%Y%H%M%S'))

        return time_now


def confirmStatus(id): # this is used to monitor the status of the computer via the database hosted on digitalocean

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
            mailOnFail.mailOnFail(id,' is not recording! Timecode - ' + dbh.getTimeOfDeath(id))
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
    dbh.setTimeOfDeath(id,setTimeOfDeath())
    mailOnFail.mailOnFail(id, ' is DOWN! Timecode - ' + dbh.getTimeOfDeath(id))
    return



