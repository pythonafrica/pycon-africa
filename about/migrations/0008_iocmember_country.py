# Generated by Django 5.0.2 on 2024-03-05 12:43

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_iocgroup_iocmember_volunteergroup_volunteer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='iocmember',
            name='country',
            field=django_countries.fields.CountryField(default='GH', max_length=2),
        ),
    ]
