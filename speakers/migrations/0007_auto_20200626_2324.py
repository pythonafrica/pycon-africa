# Generated by Django 2.2.11 on 2020-06-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0006_auto_20200626_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='country',
            field=models.CharField(blank=True, default='', help_text='City and Country the speaker is from eg. Accra, Ghana', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='profession',
            field=models.CharField(blank=True, default='', help_text="Speaker's profession. eg. Software Developer", max_length=200, null=True),
        ),
    ]
