__author__ = 'erlend'

import smtplib



def mailOnFail(id, message):


    mail = smtplib.SMTP('smtp.gmail.com',25)
    mail.ehlo()
    mail.starttls()
    mail.login('erlendwestbye@gmail.com', '***')

    mail.sendmail('erlendwestbye@gmail.com','erlendwestbye@gmail.com', id + ' '+ message)#Please check website for current status\n http://erlendwestbye.me/systemmonitor/'
    mail.close()