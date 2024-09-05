from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from datetime import datetime
from .models import Schedule, Proposal

class TalkScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'conference_day': forms.Select(attrs={'class': 'form-control'}),
            'talk': forms.Select(attrs={'class': 'form-control'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'step': '60'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'step': '60'}),
            'day_session': forms.Select(attrs={'class': 'form-control'}),
            'allocated_room': forms.Select(attrs={'class': 'form-control'}),
            'event_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter event URL'}),
            'external_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter external URL'}),
        }

    def __init__(self, *args, **kwargs):
        super(TalkScheduleForm, self).__init__(*args, **kwargs)

        # Initialize Crispy Forms helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('conference_day'),
            Field('talk'),
            Field('event'),
            Field('start_time'),
            Field('end_time'),
            Field('day_session'),
            Field('allocated_room'),
            Field('event_url'),
            Field('external_url'),
            Submit('submit', 'Save Schedule', css_class='btn btn-primary')
        )

        # Get the talks already scheduled
        scheduled_talks = Schedule.objects.filter(talk__isnull=False).values_list('talk_id', flat=True)

        # Filter available talks that haven't been scheduled and are accepted by the speaker
        available_talks = Proposal.objects.filter(status='A', user_response='A').exclude(pk__in=scheduled_talks)

        # Add available talks to the choices (id, title)
        talk_choices = [(talk.pk, talk.title) for talk in available_talks]

        # Set the available talks in the dropdown
        self.fields['talk'].choices = [('', 'Select a talk')] + talk_choices

        # Set placeholders and help texts dynamically
        self.fields['event'].widget.attrs.update({'placeholder': 'Enter event name'})
        self.fields['talk'].widget.attrs.update({'placeholder': 'Select a talk'})
