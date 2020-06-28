# Generated by Django 2.2.11 on 2020-06-27 00:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0011_auto_20200627_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiencetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience_type', models.CharField(default='', max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='talk_type',
        ),
        migrations.AddField(
            model_name='speaker',
            name='talk_type',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='speakers.Talktype'),
        ),
        migrations.AlterField(
            model_name='talktype',
            name='talk_type',
            field=models.CharField(choices=[('', ''), ('Talk', 'Talk'), ('Tutorial', 'Tutorial')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='speaker',
            name='audience_type',
            field=models.ManyToManyField(default='', to='speakers.Audiencetype'),
        ),
    ]
