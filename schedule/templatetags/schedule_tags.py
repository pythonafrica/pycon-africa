from django import template
from schedule.models import TalkSchedule, Day, ScheduleVisibility
from home.models import EventYear
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

register = template.Library()

@register.inclusion_tag('2024/schedule/schedule_home.html', takes_context=True)
def schedule_preview(context, year, limit=5):
    request = context['request']
    event_year = EventYear.objects.get(year=year)

    # Check visibility of the schedule
    visibility = ScheduleVisibility.objects.first()
    if visibility is None:
        visibility = ScheduleVisibility.objects.create(is_live=False)

    if not visibility.is_live and not request.user.is_superuser:
        # Return an empty schedule if it's not live and the user is not a superuser
        return {
            'day_schedules': [],
            'year': year,
            'limit': limit,
            'is_schedule_live': visibility.is_live or request.user.is_superuser,
        }

    days = Day.objects.all().order_by('conference_day')
    day_schedules = []

    # Fetch the schedule for each day
    for day in days:
        schedules = TalkSchedule.objects.filter(
            conference_day=day,
            talk__event_year=event_year
        ).select_related('talk', 'talk__user').prefetch_related('talk__speakers').order_by('start_time')[:limit]
        
        if schedules.exists():
            day_schedules.append({
                'day': day,
                'schedules': schedules
            })
            break  # We only need to display one day's schedule

    # Attempt to get the correct template for the year, fallback to 'partials/schedule_home.html' if it doesn't exist
    template_path = f'{year}/schedule/schedule_home.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        template_path = 'partials/schedule_home.html'

    # Pass the final context to the template
    return {
        'day_schedules': day_schedules,
        'year': year,
        'days': days,
        'limit': limit,
        'is_schedule_live': visibility.is_live,
        'template_path': template_path,
    }
