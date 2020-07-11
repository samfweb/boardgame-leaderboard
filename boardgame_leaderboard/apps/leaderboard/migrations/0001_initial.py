# Generated by Django 3.0.4 on 2020-07-11 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boardgame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('strategy', 'Strategy'), ('deckbuilding', 'Deckbuilding'), ('rpg', 'RPG')], max_length=20)),
                ('max_players', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_boardgame', to='leaderboard.Boardgame')),
                ('players', models.ManyToManyField(to='leaderboard.Player')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_winner', to='leaderboard.Player')),
            ],
        ),
    ]
