from django.db import models

# Create your models here
class Contact(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField(default=False)
    Subject=models.CharField(max_length=250,default=False)
    message=models.TextField(max_length=250)



    def __str__(self):
        return self.Subject


class Category(models.Model):
    img=models.ImageField(upload_to="upload",default=False)
    Department = models.CharField(max_length=250)

    def __str__(self):
        return self.Department

class Login(models.Model):
    name=models.CharField(max_length=20)
    Department=models.CharField(max_length=30)
    contact=models.IntegerField(default=False)
    doctorid=models.CharField(max_length=12)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.name +"   " +self.Department


class Appointment(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=200)
    Email=models.EmailField(default=False)
    Contact=models.IntegerField(default=False)
    Department=models.ForeignKey(Category,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=False)
    msg=models.TextField(max_length=300)
    def __str__(self):
        return self.name 