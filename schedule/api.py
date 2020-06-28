from rest_framework.viewsets import ModelViewSet

from .serializers import DaySerializer, TalkScheduleSerializer, TalkSerializer, EventSerializer, SpeakerSerializer
from .models import Day, TalkSchedule, Event
from speakers.models import Speaker


 
class DayViewSet(ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class TalkScheduleViewSet(ModelViewSet):
    queryset = TalkSchedule.objects.all()
    serializer_class = TalkScheduleSerializer


class SpeakerViewSet(ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    