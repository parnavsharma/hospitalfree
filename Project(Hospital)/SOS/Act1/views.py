from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.contrib import messages
import messagebox
from unicodedata import category

from.models import *
# this is for import of models

def home(request):
    return render (request,'index.html')

def cat(request):
    po=Category.objects.all()
    return render(request,'index.html',{'po':po})

def login(request):
    if request.method=="POST":
        doctorid=request.POST['doctorid']
        passw = request.POST['passw']
        if Login.objects.filter(doctorid=doctorid):
            data=Login.objects.get(doctorid=doctorid)

            request.session['hos']=doctorid
            if data.password==passw:
                mes = "You are Login Successfully"
                return render(request,'index.html',{'mes':mes})
            else:
                msg="Please check your Password"
                return render(request,'login.html',{'msg':msg})
        else:
            msg0 = "Please check your Id and Password "
            return render(request,'login.html',{'msg0':msg0})
    return render(request,'login.html')

def logout(request):
    del request.session
    return render(request,'index.html')

def forget(request):
    messagebox.showinfo("hello holla", "Please visit your HOD")
    return redirect('login')

def circlepage1(request):
    return render(request,'circlepage.html')

def appoint(request):
    if request.method=="POST":
        Name=request.POST["name"]
        Email=request.POST['email']
        date=request.POST['date']
        contac=request.POST['phone']
        department=request.POST['department']
        message=request.POST['message']

        categ=Category.objects.get(Department=department)

        Appointment.objects.create(name=Name,Email=Email,date=date,Contact=contac,Department=categ,msg=message)
        return redirect("menu")
    cat = Category.objects.all()
    return render(request, 'index.html', {'cat': cat})
