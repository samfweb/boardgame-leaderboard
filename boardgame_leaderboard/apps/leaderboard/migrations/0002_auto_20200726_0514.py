# Generated by Django 3.0.8 on 2020-07-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='players',
            new_name='player_set',
        ),
    ]
