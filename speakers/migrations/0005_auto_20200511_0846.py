# Generated by Django 2.2.11 on 2020-05-11 08:46

from django.db import migrations
import django_extensions.db.fields
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_remove_speaker_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='bio',
            new_name='biography',
        ),
        migrations.AlterField(
            model_name='speaker',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(default='default.png', upload_to='speakers/'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='talk_title'),
        ),
    ]