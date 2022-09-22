from django.urls import path
from .views import *
from .views1 import * 

urlpatterns = [
    #path('',Home, name = 'home-page'),
    #path('personal_information/',Personal_information, name= 'personal-information-page'),
    path('goods_forecasting/',Agriculture, name= 'Agriculture-page'),
    #path('experience/',Experience, name= 'Experience-page'),
    #path('education/',Education, name= 'Education-page'),
    path('coordination/',Coordination, name= 'Coordination-page'),
    path('accountant/',Accountant, name= 'Accountant-page'),
    path('register/',Register, name= 'Register-page'),
    path('profileuser/',ProfileUser, name= 'ProfileUser-page'),
    path('reset-password/',ResetPassword, name= 'reset-password'),
    path('reset-new-password/<str:token>/',ResetNewPassword, name= 'Reset-new-password'),
    path('verify-success/<str:token>/',Verify_success, name= 'verify-success'),
    path('action-detail/<int:cid>/',ActionPage, name= 'Action-page'),
    path('add-product/',AddProduct, name= 'Add-Product'),

    path('bas-bana/',Basbana, name= 'Basbana-page'),
    #path('bana-contact/',BanaContact, name= 'Bana-Contact'),
    #path('bana-accountant/',BanaAccountant, name= 'Bana-Accountant'),
    path('',BanaMygoods, name= 'Bana-Mygoods'),


    path('resume-home/',ResumeHome, name= 'Resume-Home'),
    path('about-page/',Aboutme, name= 'About-page'),
    path('history-page/',History, name= 'History-page'),
    path('example-skill/',ExampleSkill, name= 'Example-Skill'),

    #####AJAX สร้างสองตาราง คือ ตารางที่ให้เพิ่ม User และตารางอัพเดท ยังไม่มีกับบันทึกข้อมูลลงฐานดาต้าเบส ####
    path('crud-page/',CrudView.as_view(), name= 'Crud-ajax'),
    ####CreateCrudUser ตารางที่รับข้อมูลลูกค้าใน crud-page ####
    path('ajax/crud-page/create/',  CreateCruduser.as_view(), name='crud_ajax_create'),
    ####UpdateCruduser  ป๊อปอัพที่โชว์เมื่อจะแก้ไขข้อมูล ####
    path('ajax/crud-page/update/',  UpdateCruduser.as_view(), name='crud_ajax_update'),
    ####DeleteCruduser ป๊อปอัพที่โชว์เมื่อจะลบ####
    path('ajax/crud-page/delete/',  DeleteCruduser.as_view(), name='crud_ajax_delete'),
]
