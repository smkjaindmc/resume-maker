# Generated by Django 2.1.4 on 2020-04-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0017_auto_20200417_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='graduation_achievements',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='graduation_year',
            field=models.CharField(default='2017-2021', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='highest_qualification',
            field=models.CharField(default='BTECH', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='institute_name',
            field=models.CharField(default='IIIT Gwalior', max_length=50),
        ),
    ]
