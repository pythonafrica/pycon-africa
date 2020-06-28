# Generated by Django 2.2.11 on 2020-06-27 00:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('speakers', '0009_auto_20200627_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_day', models.CharField(max_length=30)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TalkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('day_session', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], default='', max_length=10)),
                ('conference_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Day')),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speakers.Speaker')),
            ],
            options={
                'verbose_name_plural': 'talk Schedule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('day_session', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], default='', max_length=10)),
                ('conference_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Day')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
