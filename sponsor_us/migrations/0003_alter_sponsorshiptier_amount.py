# Generated by Django 5.0.2 on 2024-03-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor_us', '0002_sponsorshiptier_display_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorshiptier',
            name='amount',
            field=models.IntegerField(help_text='Sponsorship Tier Amount eg, 1000.00'),
        ),
    ]
