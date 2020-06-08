from django import forms
from .models import Sponsor


class SponsorForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = ('name', 'description')
