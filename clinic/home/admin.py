from django.contrib import admin

from . models import Department ,Doctors ,Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display =('id', 'pat_name', 'pat_age','pat_phone', 'pat_symtom', 'doc_name','b_date', 'Booked_on' )

admin.site.register(Booking,BookingAdmin)



