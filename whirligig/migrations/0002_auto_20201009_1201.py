# Generated by Django 3.1 on 2020-10-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whirligig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='timer_paused_time',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='timer_time',
            field=models.BigIntegerField(default=0),
        ),
    ]
