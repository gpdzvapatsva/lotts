import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# s = smtplib.SMTP('smtp.gmail.com',587)
# sender_email_id = 'abdullahtest585@gmail.com'
# reciever_email_id = \
# f = open('PlayerID.txt','+r')
# emailthing = f.read()
# password = "testing0909"
#
# subject = "Hello All"
# msg = MIMEMultipart()
# msg ['from'] = sender_email_id
# msg ['To'] = reciever_email_id
# msg ['Subject'] = subject
# body = str(emailthing)
#
# msg.attach(MIMEText(body, 'plain'))
# text = msg.as_string()
# s.starttls()
# s.login(sender_email_id,password)
#
# s.sendmail(sender_email_id,reciever_email_id, text)
# s.quit()
#
# f.close()
f = open('PlayerID.txt','+r')
emailthing = ''
for x in f.read():
    emailthing = emailthing + x

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'lottoemail123@gmail.com'
receiver_email_id = 'jessenterblanche@gmail.com'
password = 'MonkeyVillage123'

s.starttls()

s.login(sender_email_id, password)

message = "Subject: Congratulations!!!\n"
message = message + emailthing

s.sendmail(sender_email_id, receiver_email_id, message)

s.quit()
f.close()