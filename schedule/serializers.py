from rest_framework import serializers

from schedule.models import TalkSchedule, Event, Day
from speakers.models import Talk, Speaker


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
        exclude = ('youtube_iframe_url')


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        exclude = ('company')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = all
