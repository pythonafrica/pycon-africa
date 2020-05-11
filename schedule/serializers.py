from rest_framework import serializers

from schedule.models import TalkSchedule, Event, Day
from speakers.models import Talk


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('conference_day')


class TalkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalkSchedule
        fields = all


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        exclude = ('talk_description')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = all
