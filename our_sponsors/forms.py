from django import forms
from .models import *

class SponsorForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = ('name', 'description')
