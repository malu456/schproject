from . import views
from django.urls import path
from .import views
urlpatterns = [
    path('',views.demo,name='demo'),
    path('register', views.registerUser, name='register'),
    path('login', views.login, name='login'),
     path('form',views.form,name='form'),
    path('npage',views.npage,name='npage'),
    path('msg',views.msg,name='msg')

]
