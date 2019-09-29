#Step1: IMport SMTP package(SMTPlib)
#Step2: Create an object
#Step3: Login(Username and password )
#Step4:Start session and send mail
#Step5:close session

import smtplib
s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("jyotiaryan0@gmail.com","Praku@04")
text = "Mail from python script regarding project sessions"
s.sendmail("jyotiaryan0@gmail.com","ranjanprakash4u@outlook.com",msg=text)
print("Mail sent sucessfullt..... check your inbox")
s.quit()
