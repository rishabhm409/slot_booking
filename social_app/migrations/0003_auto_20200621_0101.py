# Generated by Django 3.0.7 on 2020-06-20 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0002_auto_20200621_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliable',
            name='fulldate',
        ),
        migrations.RemoveField(
            model_name='busy',
            name='fulldate',
        ),
    ]