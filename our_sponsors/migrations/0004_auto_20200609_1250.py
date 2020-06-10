# Generated by Django 2.2.11 on 2020-06-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_sponsors', '0003_auto_20200609_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='show_biography',
            field=models.BooleanField(default=True, help_text='Untick if the company only want their logo displayed on our website. Not all companies want their information on the site, they only want a link to their site'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[('Headline', 'Headline'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze'), ('Individual', 'Individual'), ('Other', 'Other')], max_length=15),
        ),
    ]