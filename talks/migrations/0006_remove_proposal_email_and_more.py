# Generated by Django 5.0.2 on 2024-04-12 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0005_proposal_speakers_speakerinvitation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='email',
        ),
        migrations.AlterField(
            model_name='proposal',
            name='intended_audience',
            field=models.CharField(blank=True, choices=[('BGN-L', 'Beginner Level'), ('INT-L', 'Intermediate Level'), ('EXP-L', 'Expert Level'), ('GEN-L', 'General')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comments', models.TextField(blank=True)),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='talks.proposal')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='talks.reviewer')),
            ],
        ),
    ]