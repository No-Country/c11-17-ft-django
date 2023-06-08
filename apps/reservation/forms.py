from apps.reservation.models import Reservation
from django import forms
class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ('sitter',
                  'owner', 
                  'dog',
                  'start_date',
                  'end_date',)
        
        
            
        