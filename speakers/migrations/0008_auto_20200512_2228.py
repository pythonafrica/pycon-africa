# Generated by Django 2.2.11 on 2020-05-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_auto_20200512_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='talk_type',
            field=models.CharField(choices=[('', ''), ('Talk', 'Talk'), ('Tutorial', 'Tutorial')], default='', max_length=20),
        ),
    ]