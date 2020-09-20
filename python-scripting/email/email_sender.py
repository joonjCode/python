import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
#https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/



html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'niz'
email['to'] = 'jtj8081@gmail.com'
email['subject'] = 'Testing email from python'

# Content
# email.set_content('Sending email from python')
email.set_content(html.substitute({'name':'niz'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # tls : encryption
    smtp.starttls()
    smtp.login('nizin117@gmail.com', 'R]L3&fr<Qd}%')
    smtp.send_message(email)
    print('all good')

