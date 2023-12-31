import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "tejusawant302@gmail.com"
toaddr = "tejusawant307@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Interview Material"

body = """Greetings from <b>Tejas Sawant</b>,
<hr>
Python 4th week presentation to prepare for Interview. <br>
<a href="https://github.com/Tejaso7"> Github link for codes</a>
<br>
<hr>
Regards,
Tejas Sawant
"""
msg.attach(MIMEText(body, 'html'))

# Open the file to be send
filename = "Python_4th week"
attachment = open("D:/Learn/Python/Python PPt/Python 4th week.pptx","rb")

# Instance of the MIMEbase and named as p-Payload

p = MIMEBase('application','octet-stream')

# To change the payload into encodede form
p.set_payload(attachment.read())
encoders.encode_base64(p)

p.add_header('Content-Disposition',"attachment; filename= %s" %filename)
msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, " tejusawant302")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)

s.quit()

print("Sent an Attachment")
