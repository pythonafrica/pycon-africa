# Generated by Django 3.2 on 2022-08-03 03:04

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_ticket_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_image_two',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='section_one',
            field=markdownx.models.MarkdownxField(blank=True, default='', help_text='[Supports Markdown] - Ticket PyCon Africa.', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='section_two',
            field=markdownx.models.MarkdownxField(blank=True, default='', help_text='[Supports Markdown] - Ticket PyCon Africa.', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_image_one',
            field=models.ImageField(blank=True, help_text='Upload your cover image or leave blank to use our default image', null=True, upload_to='ticket_page'),
        ),
    ]
