import smtplib
emailTo = "mukundparve@gmail.com"
emailfrom = "mukundparve98@gmail.com"
loginId = "mukundparve98@gmail.com"

msg = """Congratulations Mukund! You have sent a automated mail using python"""

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(loginId, "**********")
server.sendmail(emailfrom, emailTo, msg)
server.quit()
print("Email Sent, Check your gmail")
