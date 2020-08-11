import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

EMAIL = 'junizj@gmail.com'

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    with open('password.txt', 'r') as f:
        password = f.read()

    server.login(EMAIL, password)
except :
    print('Login error')


msg = MIMEMultipart()
msg['From'] = 'Joon J '
msg['To'] = 'jtj308@naver.com'
msg['Subject'] = 'Just a test message'


with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'test.jpg'

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment, filename = {filename}')
msg.attach(p)

text = msg.as_string()
try:
    server.sendmail(EMAIL,'jtj308@naver.com', text)
    server.quit()
except:
    print('Send error')
