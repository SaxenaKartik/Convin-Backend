# Generated by Django 3.1 on 2020-08-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('task_desc', models.IntegerField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('update_type', models.IntegerField(choices=[(1, 'Daily'), (2, 'Weekly'), (3, 'Monthly')])),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'TaskTrackers',
            },
        ),
    ]
