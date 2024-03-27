from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Proposal 
from home.models import EventYear 

@receiver(post_save, sender=Proposal)
def send_status_change_email(sender, instance, created, **kwargs):
    if not created:
        try:
            original = Proposal.objects.get(pk=instance.pk)
            if original.status != instance.status:  # Check if the status has changed
                subject = 'Your Proposal Status Update'
                html_content = render_to_string('emails/talks/proposal_status_changed.html', {'proposal': instance})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(subject, text_content, to=[instance.user.email])
                email.attach_alternative(html_content, "text/html")
                email.send()
        except Proposal.DoesNotExist:
            pass  # Proposal not found, unlikely but possible during deletion
