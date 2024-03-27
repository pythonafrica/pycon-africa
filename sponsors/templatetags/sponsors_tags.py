from django import template 

register = template.Library() 
from ..models import *

@register.inclusion_tag('2022/sponsors/footer_sponsors.html')
def show_sponsor():
    sponsor = Sponsor.objects.filter(is_visible=True)
    return {'sponsor': sponsor}


@register.inclusion_tag('2022/sponsors/home_sponsors.html')
def show_home_sponsor():
    sponsor_h_home = Sponsor.objects.filter(is_visible=True, category="Headline")
    sponsor_p_home = Sponsor.objects.filter(is_visible=True, category="Platinum")
    return {'sponsor_h_home': sponsor_h_home, 'sponsor_p_home': sponsor_p_home}
