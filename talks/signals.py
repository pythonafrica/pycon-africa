from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Proposal 
from home.models import EventYear  
from django.db.models.signals import pre_save


@receiver(pre_save, sender=Proposal)
def send_status_change_email(sender, instance, **kwargs):
    if instance.pk:
        try:
            original = sender.objects.get(pk=instance.pk)
            if original.status != instance.status:
                subject_templates = {
                    'A': 'PyCon Africa - Congratulations, Your Proposal Has Been Accepted',
                    'W': 'PyCon Africa - Your Proposal Is On The Waiting List',
                    'R': 'PyCon Africa - Your Proposal Has Been Rejected',
                    'S': 'PyCon Africa - Your Proposal Has Been Submitted'
                }
                template_names = {
                    'A': 'emails/talks/proposal_accepted.html',
                    'W': 'emails/talks/proposal_waiting.html',
                    'R': 'emails/talks/proposal_rejected.html',
                    'S': 'emails/talks/proposal_submitted.html'
                }
                subject = subject_templates.get(instance.status, 'PyCon Africa - Your Proposal Status Update')
                html_template = template_names.get(instance.status, 'talks/emails/proposal_status_changed.html')
                html_content = render_to_string(html_template, {'proposal': instance, 'user': instance.user})
                text_content = strip_tags(html_content)
                
                email = EmailMultiAlternatives(
                    subject,
                    text_content,
                    'noreply@pycon.africa',
                    [instance.user.email]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
        except sender.DoesNotExist:
            pass  # Handle the case where the Proposal does not exist when the email is triggered





