from django.db import models


# Create your models here.

class Department(models.Model):
    dep_name =models.CharField(max_length=250)
    dep_des =models.TextField()
    dep_image=models.ImageField()

    def __str__(self):
        return self.dep_name
    

class Doctors(models.Model):
    doc_name =models.CharField(max_length=250)
    doc_qualificc=models.CharField(max_length=100)
    doc_dep=models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    doc_code=models.IntegerField()

    def __str__(self):
        return self.doc_name
    

class Booking(models.Model):
    pat_name =models.CharField(max_length=200)
    pat_phone=models.IntegerField()
    pat_age=models.IntegerField()
    pat_symtom=models.TextField(max_length=150)
    doc_name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    b_date=models.DateField()
    b_slot=models.IntegerField()
    Booked_on=models.DateField(auto_now=True)







