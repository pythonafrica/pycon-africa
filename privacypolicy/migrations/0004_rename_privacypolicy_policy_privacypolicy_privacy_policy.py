# Generated by Django 3.2 on 2022-03-30 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privacypolicy', '0003_auto_20220330_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privacypolicy',
            old_name='privacypolicy_policy',
            new_name='privacy_policy',
        ),
    ]