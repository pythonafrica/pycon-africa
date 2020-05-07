from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Speaker


class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Speaker
        fields = ('speaker_name', 'biography')
        widgets = {
            'biography': SummernoteWidget(),
        }

X_FRAME_OPTIONS = 'SAMEORIGIN'