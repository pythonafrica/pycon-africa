# Generated by Django 2.2.11 on 2020-05-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20200512_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='talk_title',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
