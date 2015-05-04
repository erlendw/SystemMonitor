__author__ = 'erlend'

import smtplib
import databaseHandeling as dbh


def mailOnFail(id, message):


    mail = smtplib.SMTP('smtp.gmail.com',25)
    mail.ehlo()
    mail.starttls()
    mail.login('erlendwestbye@gmail.com', '***')

    location = dbh.getLocationName(id)

    mail.sendmail('erlendwestbye@gmail.com','erlendwestbye@gmail.com', str(location) + ' ' + message)#Please check website for current status\n http://erlendwestbye.me/systemmonitor/'
    mail.close()