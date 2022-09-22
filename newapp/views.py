from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from songline import Sendline
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .sendgmail import sendthai
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

# def Home(request):
# 	return HttpResponse('<h1>Hello world</h1><br><p>By n.Khanthamalee</p>')
#def Home(request):
	#return render(request,'newapp/home.html')


#def Personal_information(request):
	#return render(request,'newapp/Personal information.html')


def Agriculture(request):
	
	allmygoods= AgricultureGoods.objects.all()

	#กำหนดว่าแต่ละ page สามารถดู product ได้กี่ชิ้น
	product_per_page = 3
	paginator = Paginator(allmygoods,product_per_page)
	page = request.GET.get('page')
	allmygoods = paginator.get_page(page)

	context = {'allmygoods':allmygoods}

	allrow = []
	row = []
	for i,p in enumerate(allmygoods):
		if i%3 == 0:
			if i != 0 :
				allrow.append(row)
			row = []
			row.append(p)
		else:
			row.append(p)
	allrow.append(row)
	context['allrow'] = allrow

	return render(request,'newapp/Agriculturegoods.html',context)

#def Experience(request):
	#return render(request,'newapp/experience.html')


#def Education(request):
	#return render(request,'newapp/education.html')

def Login(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		username = data.get('username')
		password = data.get('password')
		try:
			user = authenticate(username = username, password = password)
			login(request,user)
			return redirect('ProfileUser-page')
		except:
			context['message'] = 'Username or password incorrect!!,please check the correctness or reset your password.'

	return render(request,'newapp/login.html',context)

def Coordination(request):

	context = {}

	if request.method == 'POST':
		data = request.POST.copy()
		title = data.get('title')
		phone = data.get('phone')		
		email = data.get('email')
		detail = data.get('detail')
		print(title)
		print(phone)
		print(email)
		print(detail)
		print('-------------------')

		if email == '':
			context['message'] = ' Please enter your email.'
			return render(request,'newapp/Banacontact.html',context)

		newrecord = CoordinationList()
		newrecord.title = title
		newrecord.phone = phone
		newrecord.email = email
		newrecord.detail = detail
		newrecord.save()
		context['message'] ='I got your message,please wait to contact you back within 24 hours.'

		#ระบบส่งไลน์
		token = 'akczxnVDysRM3SDuvHwt1sqxQDA94iOpuDVCpswO3bg'
		m = Sendline(token)
		m.sendtext('\nTopic : {}\nPhone : {}\nEmail : {}\n>>> {}'.format(title,phone,email,detail))

		#ระบบส่ง gmail ที่ใช้ app_generate_password
		text = 'สวัสดีค่ะ \nน้องน้อย AI ได้รับข้อมูลเรียบร้อยแล้ว\nเดี๋ยวจะรีบตอบกลับนะคะ'
		sendthai(email,'น้องน้อย AI',text)


	return render(request,'newapp/coordination.html',context)

@login_required
def Accountant(request):
	contact= CoordinationList.objects.all().order_by('-id')
		#contact= CoordinationList.objects.all()
	context = {'contact':contact}
	return render(request,'newapp/accountant.html',context)

def Register(request):
	context = {}

	if request.method == 'POST':
		#รับข้อมูลจาก Register.html
		data = request.POST.copy()
		fullname = data.get('fullname')
		mobile = data.get('mobile')
		username = data.get('username')
		password = data.get('password')
		password2 = data.get('password2')


		try: 
			check = User.objects.get(username=username)   #ตรวจสอบว่ามี email นี้ในระบบหลังบ้านเราไหม
			context['warning']='You can not use {}, Please use a new e-mail'.format(username)
			return render(request,'newapp/Register.html',context)   #ถ้าไม่มีให้ปรากฏ warning และหน้า Register.html

		except:

			#ถ้ายังไม่มี email นี้ในระบบหลังบ้านให้ >>

			# 1. ตรวจสอบ password
			if password != password2:   #ตรวจสอบ password ว่าถูกต้องไหม
				context['warning']='Please enter the same password'
				return render(request,'newapp/Register.html',context) #ถ้าไม่มีให้ปรากฏ warning และหน้า Register.html

			# 2. เพิ่มข้อมูลใน User
			newuser = User()    #User ใหม่ คือ User ในหลังบ้าน 
			newuser.username = username    #email ใหม่ใน Register.html คือ username ในหลังบ้าน 
			newuser.email = username     #email ใหม่ใน Register.html คือ email ในหลังบ้าน
			newuser.first_name = fullname   #fullname ใหม่ใน Register.html คือ first_name ในหลังบ้าน
			newuser.set_password(password)  #password ใหม่ใน Register.html คือ set_password ในหลังบ้าน 
			                                #> set_password(password ใน html)
			newuser.save()    #บันทึกข้อมูลทั้งหมด

			u = uuid.uuid1()
			token = str(u)  #สุ่ม

			# 3. เพิ่มข้อมูลใน Profile
			newprofile = Profile()    #สร้างโปรไฟล์ใหม่หลังจากมีการสมัครสามาชิก
			newprofile.user = User.objects.get(username=username)    #รับ username เป็น email จาก Register.html ใน User
			                                                         #มาเป็น user ใน profile
			newprofile.mobile = mobile    #mobile เป็น mobile ใหม่จาก Register.html จะบันทึกใน mobile class Profile
			newprofile.verify_token = token
			newprofile.save() #บันทึกข้อมูลทั้งหมด


			#ถ้าสมัครสมาชิกแล้ว จะปรากฏ text ใน email ดังนี้ 
			text = 'Please enter this link for confirmation of membership at n.Khanthamalee website\n\n Link: http://localhost:8000/verify-success/'+token
			sendthai(username,'n.Khanthamalee Website',text)

		try:
			user = authenticate(username = username, password = password)
			login (request,user)
			return redirect('ProfileUser-page')
		except:
			context['message'] = 'Username or Password incorrect'

	return render(request,'newapp/Register.html',context)

def Verify_success(request,token):
	context = {}

	try:
		check = Profile.objects.get(verify_token = token)
		check.verified = True
		check.point = 100
		check.save()

	except:
		context['error'] = 'This is not confirmation link, please click link from your e-mail.'

	return render(request,'newapp/verifyemail.html',context)


@login_required
def ProfileUser(request): #ใช้ Profile ไม่ได้เพราะ class model มีชื่อนี้แล้ว
	context = {}
	profileuser = Profile.objects.get(user=request.user)
	context['profile'] = profileuser
	return render(request,'newapp/profile.html',context)

import uuid
def ResetPassword(request):

	context = {}

	if request.method == 'POST':
		#รับข้อมูลจาก resetpassword.html
		data = request.POST.copy()
		username = data.get('username')

		try: 
			user = User.objects.get(username=username)   #ตรวจสอบว่ามี email นี้ในระบบหลังบ้านเราไหม
			u = uuid.uuid1()
			token = str(u)
			newreset = ResetPasswordToken()
			newreset.user = user
			newreset.token = token
			newreset.save()

			#ข้อความใน e-mail ของ username ที่ต้องการ reset password
			text = 'Please click this link for reset password.\n\nLink : http://localhost:8000/reset-new-password/'+token
			sendthai(username,'resetpassword link(n.Khanthamalee)',text)

			#ข้อความบน reset-password ที่จะปรากฏเมื่อเรากรอก username เรียบร้อยแล้ว
			context['message'] = 'The reset password link was send to you e.mail, please check the last your e-mail.'
			return render(request,'newapp/resetpassword.html',context)

		except:
			#ข้อความบน reset-password ที่จะปรากฏเมื่อเรากรอก username ที่ไม่มีในระบบ database
			context['message'] = 'Your e-mail has not the system, please check the correctness'

	return render(request,'newapp/resetpassword.html',context)

def ResetNewPassword(request,token):

	context = {}
	print('token:',token)

	try:
		check = ResetPasswordToken.objects.get(token=token)   #ตรวจสอบว่า token = token ใน database ไหม

		#ดึงข้อมูลจาก reset-new-password 
		if request.method == 'POST':
			data = request.POST.copy()
			password1 = data.get('resetpassword1')
			password2 = data.get('resetpassword2')

			if password1 == password2:    #ถ้า password ทั้งสองเหมือนกันให้ทำต่อไป
				user = check.user    #user เท่า user ใน model ResetPasswordToken 
				user.set_password(password1)   #set password1 เป็น password ของ user
				user.save()    #บันทึกข้อมูลง database
				user = authenticate(username=user.username,password=password1) 
				login(request,user)
				return redirect('ProfileUser-page')   #login แล้วปรากฏหน้า ProfileUser-page

			else:    #ถ้า password ทั้งสองไม่เหมือนกันให้ เตือน error บน reset-new-password
				context['error'] = 'Please enter the same password.'

	except:    #ถ้าหน้าที่เข้าไปเพืท่อ reset password ไม่ใช่ token ใน database จะปรากฏข้อความ

		#แล้วบอกให้ reset password ใหม่อีกครั้ง ซึ่ง return เข้าหน้า resetpassword ให้แล้ว
		context['error'] = 'Reset password link incorrect, please reset password again'
		return render(request,'newapp/resetpassword.html',context)  

	return render(request,'newapp/resetnewpassword.html',context)

@login_required
def ActionPage(request,cid):
	#cid = CoordinationList id
	context = {}

	coordination = CoordinationList.objects.get(id=cid)
	context['coordination']=coordination 

	try:
		action = Action.objects.get(coordinationaction=coordination)
		context['action']= action

	except:
		pass

	if request.method =='POST':
		data = request.POST.copy()
		detail = data.get('detail2')

		if 'save' in data:
			try:
				check = Action.objects.get(coordinationaction=coordination)
				check.actiondetail = detail
				context['action']=check
				check.save()
				return redirect('Accountant-page')
			except:
				new = Action()
				new.coordinationaction = coordination
				new.actiondetail = detail
				context['action']=new
				new.save()

		elif 'delete' in data:
			try:
				coordination.delete()
				return redirect('Accountant-page')
			except:
				pass

		elif 'completed' in data:
			coordination.complete = True
			coordination.save()
			return redirect('Accountant-page')

	return render(request,'newapp/action.html',context)

def Basbana(request):
	return render(request,'newapp/basbana.html')

#Add Product
@login_required
def AddProduct(request):
	if request.method == 'POST':
		data = request.POST.copy()
		goods = data.get('goods')
		description = data.get('description')
		price = data.get('price')
		quantity = data.get('quantity')
		instock = data.get('instock')

		print(goods)
		print(description)
		print(price)
		print(quantity)
		print(instock)
		print('File:',request.FILES)

		new = AgricultureGoods()
		new.goods = goods
		new.description =description
		new.price = float(price)
		new.quantity = int(quantity)

		if instock == 'instock':
			new.instock = True

		if 'picture' in request.FILES:
			file_image = request.FILES['picture']
			file_image_name = file_image.name.replace(' ','')
			fs = FileSystemStorage(location='media/product')
			filename = fs.save(file_image_name,file_image)
			upload_file_url = fs.url(filename)
			new.picture = '/product' + upload_file_url[6:]
			print('upload_file_url[6:]:',upload_file_url[6:])

		if 'specfile' in request.FILES:
			file_image = request.FILES['specfile']
			file_image_name = file_image.name.replace(' ','')
			fs = FileSystemStorage(location='media/specfile')
			filename = fs.save(file_image_name,file_image)
			upload_file_url = fs.url(filename)
			new.specfile = '/specfile' + upload_file_url[6:]
			print('upload_file_url[6:]:',upload_file_url[6:])

		new.save()


	return render(request,'newapp/addproduct.html')