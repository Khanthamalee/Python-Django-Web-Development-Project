#################ส่งเมลล์ภาษาไทย########################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	myemail = 'm.khantha1234@gmail.com'
	mypassword = 'avagtcbrpnnlzvdj'
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'Uncle Engineer'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP_SSL("smtp.gmail.com", 465)

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()


###########Start sending#############
subject = 'ลุง!! เงินผมหมดแล้วววว'

msg = '''สวัสดีครับ
ทดสอบส่งข้อความ
'''

sendthai('n.Khanthamalee@gmail.com',subject,msg)

# หากต้องการส่งหลายคนสามารถใส่คอมม่าใน string ได้เลย เช่น 'loongTu1@gmail.com,loongTu2@gmail.com'


'''
-------------------------
ตั้งค่าให้เป็นสีเขียวก่อนส่ง แล้วลองรีเฟรชดู ( on )
https://myaccount.google.com/lesssecureapps
'''
