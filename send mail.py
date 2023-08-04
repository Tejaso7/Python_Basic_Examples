import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = '''Hello <b>Mukund</b>'''
sender_address = 'mukundparve98@gmail.com'
sender_pass = '**********'
receiver_address = 'mukundparve@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Cc'] = "mukundparve30@gmail.com"
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The body and the attachments for the mail
message.attach(MIMEText(msg, 'html'))
#Create SMTP session for sending the mail
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls() #enable security
server.login(sender_address, sender_pass)
text = message.as_string()
server.sendmail(sender_address, receiver_address,text)
server.quit()
print('Mail Sent')
