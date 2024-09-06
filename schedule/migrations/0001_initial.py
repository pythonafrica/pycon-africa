# Generated by Django 5.0.2 on 2024-09-05 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talks', '0018_alter_proposal_talk_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_day', models.CharField(help_text='The name of the conference day (e.g., Day 1, Day 2).', max_length=30, unique=True)),
                ('actual_date', models.DateField(default='2024-09-09', help_text='The actual date of the conference day.')),
            ],
            options={
                'verbose_name': 'Conference Day',
                'verbose_name_plural': 'Conference Days',
                'ordering': ['actual_date'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, help_text='The name or number of the conference room.', max_length=50, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['room_name'],
            },
        ),
        migrations.CreateModel(
            name='ScheduleVisibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_live', models.BooleanField(default=False, help_text='Indicates if the schedule is live and visible to all users.')),
            ],
            options={
                'verbose_name': 'Schedule Visibility',
                'verbose_name_plural': 'Schedule Visibility',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(blank=True, default='', help_text='The name of the event or activity.', max_length=255)),
                ('event_description', models.TextField(blank=True, help_text='A short description of the event.')),
                ('is_an_event', models.BooleanField(default=False, help_text='Indicate if this is an event instead of a talk.')),
                ('fa_icon', models.CharField(blank=True, default='', max_length=100)),
                ('event_url', models.CharField(blank=True, default='', help_text='URL to the event', max_length=250)),
                ('external_url', models.CharField(blank=True, default='', help_text='External link to the event', max_length=250)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('day_session', models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], default='', max_length=10)),
                ('rowspan', models.CharField(blank=True, default='', help_text='Use to determine how this talk fits in its time allocation', max_length=10)),
                ('concurrent_talk', models.BooleanField(default=False)),
                ('is_a_keynote_speaker', models.BooleanField(default=False)),
                ('is_a_panel', models.BooleanField(default=False)),
                ('allocated_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.room')),
                ('conference_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.day')),
                ('talk', models.ForeignKey(blank=True, help_text="Select a Talk if it's a Speaker giving a talk", null=True, on_delete=django.db.models.deletion.CASCADE, to='talks.proposal')),
            ],
            options={
                'verbose_name_plural': 'Talk Schedules',
                'permissions': [('can_manage_schedule', 'Can manage schedules')],
                'managed': True,
                'indexes': [models.Index(fields=['start_time', 'end_time'], name='schedule_sc_start_t_f5c19e_idx')],
            },
        ),
    ]
