from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pat_name', 'pat_age','pat_phone', 'pat_symtom', 'doc_name', 'b_date', 'b_slot', 'pat_age']
        
        
        widgets = {
            'b_date': DateInput(),
        }

        labels = {
           'pat_name':'Patient Name',
           'pat_phone':'Phone Number',
           'pat_age':'Patient age',
           'doc_name':'Doctor Name',
           'b_date':'Booking Date',
           'Pat symtom':'Symtoms',
           'b_slot' : 'Time',
        }





