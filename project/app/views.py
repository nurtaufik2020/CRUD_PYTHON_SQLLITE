from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

#Create Your Views here
def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
    

def insertData(request):
    # print(context)
    # untuk menangkap data dari form
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Berhasil Ditambahkan")
        return redirect("/")
    return render(request,"index.html")


def updateData(request,id):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Berhasil Diupdate")
        return redirect("/")    
    
    d=Student.objects.get(id=id)
    context={"d":d}    
    return render(request,"edit.html",context)


def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Berhasil Dihapus")
    return redirect("/")


def about(request):
    return render(request,"about.html")

