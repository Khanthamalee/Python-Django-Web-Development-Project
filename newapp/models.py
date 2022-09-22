from django.db import models
from django.contrib.auth.models import User

'''
AgricultureGoods
	goods(char)
	description(char)
	price(decimal)
	quantity(int)
'''

class AgricultureGoods(models.Model):
	goods = models.CharField(max_length=200)
	description = models.TextField(null=True,blank=True)
	price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	instok = models.BooleanField(default=True)
	#เพิ่ม file
	picture = models.ImageField(upload_to ='product',null=True,blank=True)
	specfile = models.FileField(upload_to ='specfile',null=True,blank=True)
	
	def __str__(self):
		return self.goods

class CoordinationList(models.Model):
	title =  models.CharField(max_length=200)
	phone = models.CharField(max_length=11)
	email = models.CharField(max_length=200)
	detail = models.TextField(default=True)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	usertype = models.CharField(max_length = 100, default= 'member')
	point = models.IntegerField(default=0)
	mobile = models.CharField(max_length = 20,null=True,blank=True)
	verified = models.BooleanField(default=False)
	verify_token = models.CharField(max_length = 100,default='no  token')

	def __str__(self):
		return self.user.username

class ResetPasswordToken(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	token = models.CharField(max_length=100)
	
	def __str__(self):
		return self.user.username

class Action(models.Model):
	coordinationaction = models.ForeignKey(CoordinationList,on_delete=models.CASCADE)
	actiondetail = models.TextField()

	def __str__(self):
		return '{}-{}'.format(self.coordinationaction,self.actiondetail)


####AJAX#####
class Cruduser(models.Model):
	name = models.CharField(max_length=30, blank=True)
	address = models.CharField(max_length=100,blank=True)
	age = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.name
