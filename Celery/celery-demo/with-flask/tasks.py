import smtplib
from flaskapp import flask_celery
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#: config
username = "sibejobudiman@gmail.com"
password = "bejopunyaemail"


@flask_celery.task
def sendmail(to, subject, message):

    fromaddr = 'sibejobudiman@gmail.com'

    msg = MIMEMultipart('alternative')
    msg['From'] = fromaddr
    msg['To'] = to
    msg['Subject'] = '{} \n'.format(subject)

    part1 = MIMEText(message, 'plain')
    part2 = MIMEText(message, 'html')
    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username, password)

    print "sending email..."
    server.sendmail(fromaddr, to, msg.as_string())
    server.quit()
    print "done"
