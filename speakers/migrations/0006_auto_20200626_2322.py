# Generated by Django 2.2.11 on 2020-06-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0005_auto_20200626_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='company',
            new_name='profession',
        ),
        migrations.AddField(
            model_name='speaker',
            name='country',
            field=models.CharField(blank=True, default='', help_text='Name of Organization speaker is from. eg. Google', max_length=100, null=True),
        ),
    ]
