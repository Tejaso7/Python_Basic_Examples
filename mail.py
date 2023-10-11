import smtplib
emailTo = "tejusawant307@gmail.com"
emailfrom = "tejusawant302@gmail.com"
loginId = "tejusawant302@gmail.com"

msg = """Congratulations Tejas! You have sent a automated mail using python"""

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(loginId, "**********")
server.sendmail(emailfrom, emailTo, msg)
server.quit()
print("Email Sent, Check your gmail")
