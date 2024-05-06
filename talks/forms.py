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
        fields = ('title', 'talk_type', 'talk_category', 'intended_audience', 'elevator_pitch',  'talk_abstract',  'anything_else_you_want_to_tell_us', 'special_requirements', 'recording_release',)

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)

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
        fields = ['score', 'comments']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('score', css_class='form-group col-md-6 mb-0'),
                Column('comments', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit Review')
        )


class DocumentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Document
        fields = ('description', 'document', )
