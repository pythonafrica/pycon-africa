from django import template
from registration.models import Profile
from django.db.models import Q
import random

register = template.Library()

@register.simple_tag
def get_speakers():
    keynote_speakers = Profile.objects.filter(
        Q(user__proposals__talk_type="Keynote Speaker"),
        Q(user__proposals__status='A'),
        Q(user__proposals__user_response='A'),
        Q(is_visible=True)
    ).distinct()

    other_speakers = Profile.objects.filter(
        Q(user__proposals__status='A'),
        Q(user__proposals__user_response='A'), 
    ).exclude(
        user__proposals__talk_type="Keynote Speaker"
    ).distinct()

    # Shuffle and pick 4 random other speakers
    other_speakers = list(other_speakers)
    random.shuffle(other_speakers)
    other_speakers = other_speakers[:4]

    return keynote_speakers, other_speakers
