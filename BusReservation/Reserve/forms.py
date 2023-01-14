from django import forms

class SeatRegisterForm(forms.Form):
    bus_number=forms.IntegerField()
    seat_num=forms.IntegerField()

   