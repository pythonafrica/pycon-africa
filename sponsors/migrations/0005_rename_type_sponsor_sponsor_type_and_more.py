# Generated by Django 5.0.2 on 2024-03-17 01:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_pyconevent'),
        ('sponsor_us', '0006_alter_sponsorshiptier_no_available'),
        ('sponsors', '0004_alter_sponsor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='type',
            new_name='sponsor_type',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='category',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='event_year',
            field=models.ForeignKey(default='2024', on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to='home.eventyear'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='tier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sponsor_us.sponsorshiptier', verbose_name='sponsorship tier'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='linkedin',
            field=models.CharField(blank=True, default='', help_text="Please enter only the user name eg.'mawy_7'", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='twitter',
            field=models.CharField(blank=True, default='', help_text="Please enter only the user name eg.'mawy_7'", max_length=100, null=True),
        ),
    ]