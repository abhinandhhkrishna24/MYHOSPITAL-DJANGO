from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('doctors', views.doctors, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='department'),
    path('booking', views.booking, name='booking'),
    #path('signup', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('bookinglist', views.booking_list, name='booking_list'),
    
]