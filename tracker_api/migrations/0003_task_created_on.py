# Generated by Django 3.1 on 2020-08-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_api', '0002_auto_20200809_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
