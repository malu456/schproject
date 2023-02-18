from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Form
from .forms import RegisterForm


# Create your views here.
def demo(request):
    return render(request,"index.html")
def registerUser(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user.save();
            return redirect('npage')
        else:
           messages.info(request,"invalid credentials")
           return redirect('login')

    else:
        return render(request,'login.html')

def npage(request):
    return render(request,'newpage.html')
def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phnum = request.POST.get('phnum')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        courses = request.POST.get('courses')
        purpose = request.POST.get('purpose')
        MaterialsProvide = request.POST.get('MaterialsProvide')
        if User is not None:
           fm = Form(name=name, dob=dob, age=age, gender=gender, phnum=phnum, mail=email, address=address,
                  department=department, courses=courses, purpose=purpose, mp=MaterialsProvide)
           fm.save()
           return redirect('msg')
        else:
            messages.info(request,"enter all details")
            return redirect('form')

    else:
        return render(request, "form.html")

def msg(request):
    return render(request,'msg.html')