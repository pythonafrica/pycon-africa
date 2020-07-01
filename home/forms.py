from django import forms
from .models import KeynoteSpeaker


class KeynoteSpeakerForm(forms.ModelForm):

    class Meta:
        model = KeynoteSpeaker
        fields = ('speaker_name', 'biography')
