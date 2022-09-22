import smtplib
from email.message import EmailMessage

msg= EmailMessage()

my_address ="m.khantha1234@gmail.com"    #sender address

app_generated_password = "avagtcbrpnnlzvdj"    # gmail generated password

msg["Subject"] ="n.Khanthamalee"   #email subject 

msg["From"]= my_address      #sender address

msg["To"] = "n.khanthamalee@gmail.com"     #reciver address

msg.set_content("สวัสดีค่ะ\nได้รับข้อมูลเรียบร้อยแล้ว\nเดี๋ยวน้องน้อย AI จะรีบส่งข้อมูลตอบกลับนะคะ")   #message body

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    
    smtp.login(my_address,app_generated_password)    #login gmail account
    
    print("sending mail")
    smtp.send_message(msg)   #send message 
    print("mail has sent")