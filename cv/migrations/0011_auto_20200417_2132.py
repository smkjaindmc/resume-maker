# Generated by Django 2.1.4 on 2020-04-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_auto_20200417_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='present_role',
            field=models.CharField(choices=[('FR', 'Developer'), ('SO', 'Android_Developer'), ('JR', ' IOS_Developer'), ('SR', 'Frontend_Developer'), ('GR', 'Data_Scientist'), ('SW', 'Software_Developer')], default='FR', max_length=2),
        ),
        migrations.AlterField(
            model_name='resume',
            name='previous_role',
            field=models.CharField(choices=[('FR', 'Developer'), ('SO', 'Android_Developer'), ('JR', ' IOS_Developer'), ('SR', 'Frontend_Developer'), ('GR', 'Data_Scientist'), ('SW', 'Software_Developer')], default='GR', max_length=2),
        ),
    ]