# Generated by Django 2.2.11 on 2024-02-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20240226_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyConEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('flag_image', models.ImageField(default='flag.jpg', upload_to='countryflags/')),
                ('city', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('year', models.IntegerField()),
                ('website_url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]
