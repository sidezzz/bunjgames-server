# Generated by Django 3.1 on 2020-09-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whirligig', '0002_remove_game_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='timer_paused',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='game',
            name='timer_time',
            field=models.IntegerField(default=0),
        ),
    ]
