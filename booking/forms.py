from django import forms
from .models import Boooking


class BookingForm(forms.ModelForm):
    start_time = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    end_time = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Boooking
        fields = ['room_id', 'no_of_users', 'start_time', 'end_time']
