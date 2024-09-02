from django import forms
from .models import TalkSchedule, Proposal

class TalkScheduleForm(forms.ModelForm):
    class Meta:
        model = TalkSchedule
        fields = '__all__'  # or specify the fields you want

    def __init__(self, *args, **kwargs):
        super(TalkScheduleForm, self).__init__(*args, **kwargs)
        # Filter the talk field to only include accepted proposals
        self.fields['talk'].queryset = Proposal.objects.filter(status='A', user_response='A')
