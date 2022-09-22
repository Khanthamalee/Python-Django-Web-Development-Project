#################ส่งเมลล์ภาษาไทย########################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	myemail = 'Jzmmhjz16424@gmail.com'
	mypassword = 'zjthflztbczkvprr'
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'n.Khanthamalee'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP_SSL("smtp.gmail.com", 465)

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()

# หากต้องการส่งหลายคนสามารถใส่คอมม่าใน string ได้เลย เช่น 'loongTu1@gmail.com,loongTu2@gmail.com'


'''
-------------------------
ตั้งค่าให้เป็นสีเขียวก่อนส่ง แล้วลองรีเฟรชดู ( on )
https://myaccount.google.com/lesssecureapps
'''
