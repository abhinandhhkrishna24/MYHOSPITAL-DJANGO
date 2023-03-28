from django.shortcuts import render, redirect
from .models import Doctors, Department, Booking
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('booking_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})    
        