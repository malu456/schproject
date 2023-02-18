from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(auto_now_add=True)
    age =models.CharField(max_length=250)
    gender = models.CharField(max_length=250,default=False)
    phnum = models.CharField(max_length=250)
    mail = models.EmailField(max_length=200)
    address = models.TextField()
    department = models.CharField(max_length=250)
    courses = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    mp = models.CharField(max_length=250)