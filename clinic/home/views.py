from ast import Return
from enum import Flag
from django.shortcuts import render
from .models import Doctors, Department 
from.forms import AppointmentForm



# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def doctors(request):
    dict_doc={
        'doc' : Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_doc)

def contact(request):
    return render(request, 'contact.html')

def department(request):
   dict_dep={
       'dep' : Department.objects.all()
   } 
   return render(request, 'department.html',dict_dep)

def booking(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return render(request, 'confirmation.html')
    form = AppointmentForm()
    dict_form={
        'form': form
    }
    
    return render(request, 'booking.html', dict_form)
        