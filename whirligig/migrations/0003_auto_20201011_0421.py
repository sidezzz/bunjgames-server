# Generated by Django 3.1 on 2020-10-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whirligig', '0002_auto_20201009_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameitem',
            options={'ordering': ['number']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['number']},
        ),
        migrations.AddField(
            model_name='game',
            name='cur_random_item',
            field=models.IntegerField(default=None, null=True),
        ),
    ]