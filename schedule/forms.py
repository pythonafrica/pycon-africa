from django import forms
from .models import TalkSchedule, Proposal
from event.models import Event

class TalkScheduleForm(forms.ModelForm):
    class Meta:
        model = TalkSchedule
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TalkScheduleForm, self).__init__(*args, **kwargs)

        # Exclude talks that are already in the schedule
        scheduled_talks = TalkSchedule.objects.values_list('talk_id', flat=True)
        self.fields['talk'].queryset = Proposal.objects.filter(status='A', user_response='A').exclude(pk__in=scheduled_talks)

        # Exclude events that are already in the schedule (optional, if needed)
        scheduled_events = TalkSchedule.objects.values_list('event_id', flat=True)
        self.fields['event'].queryset = Event.objects.exclude(pk__in=scheduled_events)
 

    def clean(self):
        cleaned_data = super().clean()
        is_an_event = cleaned_data.get('is_an_event')
        event = cleaned_data.get('event')
        talk = cleaned_data.get('talk')

        # Validate that either an event or a talk is provided, but not both
        if is_an_event and not event:
            self.add_error('event', 'This field is required for events.')

        if not is_an_event and not talk:
            self.add_error('talk', 'This field is required for talks.')

        if is_an_event and talk:
            raise forms.ValidationError('You cannot have both a talk and an event in the same schedule entry.')

        return cleaned_data