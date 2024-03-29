# Generated by Django 3.2 on 2022-08-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20220803_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_image_one',
            field=models.ImageField(blank=True, default='tickets.png', help_text='Upload your cover image or leave blank to use our default image', null=True, upload_to='ticket_page'),
        ),
    ]
