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

####AJAXCrudView####
from django.views.generic import ListView

####CreateCrudUser####
from django.views.generic import View
from django.http import JsonResponse

#def BanaContact(request):
	#return render(request,'newapp/Banacontact.html')

#def BanaAccountant(request):
	#return render(request,'newapp/Banaaccountant.html')

def BanaMygoods(request):
	allgoods= AgricultureGoods.objects.all()

	product_per_page = 1
	paginator = Paginator(allgoods,product_per_page)
	page = request.GET.get('page')
	allgoods = paginator.get_page(page)

	context = {'allgoods':allgoods}
	return render(request,'newapp/Banamygoods.html',context)

def ResumeHome(request):
	return render(request,'newapp/resumehome.html')

def Aboutme(request):
	return render(request,'newapp/resumeabout.html')

def History(request):
	return render(request,'newapp/resumehistory.html')


def ExampleSkill(request):
	return render(request,'newapp/exampleskill.html')

#ดึงข้อมูลจากโมเดลและ crud.html มา
class CrudView(ListView):
    model = Cruduser
    template_name = 'newapp/crud.html'
    context_object_name = 'users'


#รับข้อมูลจาก crud.html แล้วเอาไปเขียนในฐานข้อมูล
class CreateCruduser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Cruduser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


#อัพเดทเดต้า ป๊อปอัพในการอัพเดท ที่เราคลิก Edit#
class UpdateCruduser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Cruduser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

#ลบข้อมูล  ป๊อปอัพจะโชวเมื่อเราคลิก Delete #
class DeleteCruduser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Cruduser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data) 