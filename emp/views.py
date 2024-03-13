from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import emp
# Create your views here.

def emp_home(request):
    
    emps=emp.objects.all()
 
    return render(request,"emp/home.html",{'emps':emps})
    
def add_emp(request):
    if request.method == "POST":
        
        #data featch

        emp_name= request.POST.get("emp_name")
        emp_id= request.POST.get("emp_id")
        emp_address=request.POST.get("emp_address")
        emp_phone=request.POST.get("emp_phone")
        emp_department=request.POST.get("emp_department")
        emp_working=request.POST.get("emp_working")

        #create a model object
        e=emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address = emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        
        #save the object

        e.save()

        return redirect("/emp/home/")
    
    return render(request,'emp/add_emp.html',{})


def delete_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    Emp.delete()
    return redirect("/emp/home/")


def update_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html" ,{'emp':Emp})

def do_update_emp(request ,emp_id):
    if request.method=="POST":
        emp_name= request.POST.get("emp_name")
        emp_id_temp= request.POST.get("emp_id")
        emp_address=request.POST.get("emp_address")
        emp_phone=request.POST.get("emp_phone")
        emp_department=request.POST.get("emp_department")
        emp_working=request.POST.get("emp_working")

        e=emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address = emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect ("/emp/home")