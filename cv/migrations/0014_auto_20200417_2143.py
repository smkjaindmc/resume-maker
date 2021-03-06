# Generated by Django 2.1.4 on 2020-04-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0013_auto_20200417_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='present_role',
            field=models.CharField(choices=[('Full Stack Developer', 'Developer'), ('Android Developer', 'Android_Developer'), ('IOS Developer', ' IOS_Developer'), ('Frontend Developer', 'Frontend_Developer'), ('Data Scientist', 'Data_Scientist'), ('Software Developer', 'Software_Developer')], default='Full Stack Developer', max_length=2),
        ),
        migrations.AlterField(
            model_name='resume',
            name='previous_role',
            field=models.CharField(choices=[('Full Stack Developer', 'Developer'), ('Android Developer', 'Android_Developer'), ('IOS Developer', ' IOS_Developer'), ('Frontend Developer', 'Frontend_Developer'), ('Data Scientist', 'Data_Scientist'), ('Software Developer', 'Software_Developer')], default='Data Scientist', max_length=2),
        ),
    ]
