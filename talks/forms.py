from talks.models import Proposal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Document  
from django_recaptcha.fields import ReCaptchaField 
from django_recaptcha.widgets import ReCaptchaV2Invisible  
from .models import *

class ProposalForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Proposal
        fields = ('title', 'talk_type', 'talk_category', 'intended_audience', 'elevator_pitch', 'talk_abstract', 'anything_else_you_want_to_tell_us', 'special_requirements', 'recording_release')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProposalForm, self).__init__(*args, **kwargs)
        
        if user and not user.is_staff:
            self.fields['talk_type'].choices = [
                ('Lightning Talk', "Lightning Talk - 5 mins"),
                ('Short Talk', "Short Talk - 30 mins"),
                ('Long Talk', "Long Talk - 45 mins"),
                ('Tutorial', "Tutorial - 2 hours"),
            ]

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_ProposalForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Submit'))
 


class UpdateForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Proposal
        fields = ('title', 'talk_type', 'talk_category', 'intended_audience',  'talk_abstract',   'anything_else_you_want_to_tell_us', 'recording_release',)
 
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_UpdateForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('update', 'Update Proposal'))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comments']

    sub_scores = forms.ModelMultipleChoiceField(
        queryset=SubScore.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('comments', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'sub_scores',
            Submit('submit', 'Submit Review')
        )
        if self.instance.pk:
            self.fields['sub_scores'].queryset = self.instance.sub_scores.all()

    def save(self, commit=True):
        instance = super(ReviewForm, self).save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class SubScoreForm(forms.ModelForm):
    class Meta:
        model = SubScore
        fields = ['name', 'score']

SubScoreFormSet = forms.inlineformset_factory(Review, SubScore, form=SubScoreForm, extra=1, can_delete=True)


class DocumentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Document
        fields = ('description', 'document', )
