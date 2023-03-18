#use sptp servers
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = MIMEMultipart()
email['From'] = 'your email'
email['To'] =  'to email'
email['Subject'] = Header('your title','utf-8')

text = 'your text'
email.attach(MIMEText(text,'plain','utf-8'))
smtp_o = smtplib.SMTP_SSL('your email website',465)
smtp_o.login('your email', 'your password')
smtp_o.sendmail('your email', 'to email', email.as_string())
