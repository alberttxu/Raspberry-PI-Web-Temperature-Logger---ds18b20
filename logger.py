#!/usr/bin/env python
import smtplib
from time import strftime 
from therm import read_temp

log_file = "/var/www/html/temp_data.dat"

def email_notify(temp):
    passwd = "7CHpdOk6rDo8"

    mail_to = "albert.t.xu@gmail.com"
    mail_from = "albert.t.xu@gmail.com"

    subject = "temperature log"
    body = "temp is %s C" % temp
    message = "Subject: %s\n\n%s" % (subject, body)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(mail_from, passwd)

    s.sendmail(mail_from, mail_to, message)
    s.quit()

if __name__ == '__main__':
    temp = read_temp()
    
    #if temp > 27:
    #    email_notify(temp)

    with open(log_file, 'a') as f:
        f.write(strftime("%H:%M " + temp + '\n'))
