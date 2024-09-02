from django import forms
from .models import TalkSchedule, Proposal

class TalkScheduleForm(forms.ModelForm):
    class Meta:
        model = TalkSchedule
        fields = '__all__'  # or specify the fields you want

    def __init__(self, *args, **kwargs):
        super(TalkScheduleForm, self).__init__(*args, **kwargs)
        
        # Exclude talks already in the schedule
        scheduled_talks = TalkSchedule.objects.values_list('talk_id', flat=True)
        self.fields['talk'].queryset = Proposal.objects.filter(status='A', user_response='A').exclude(pk__in=scheduled_talks)
        
        # Make the 'event' field required only if 'is_an_event' is checked
        if not self.instance.is_an_event:
            self.fields['event'].required = False
        else:
            self.fields['talk'].required = False

    def clean(self):
        cleaned_data = super().clean()
        is_an_event = cleaned_data.get('is_an_event')
        event = cleaned_data.get('event')
        talk = cleaned_data.get('talk')

        if is_an_event and not event:
            self.add_error('event', 'This field is required for events.')
        
        if not is_an_event and not talk:
            self.add_error('talk', 'This field is required for talks.')
        
        return cleaned_data