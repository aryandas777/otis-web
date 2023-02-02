# Generated by Django 4.1.5 on 2023-02-02 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HanabiContest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "variant_id",
                    models.PositiveIntegerField(
                        help_text="The ID of the variant to play."
                    ),
                ),
                (
                    "variant_name",
                    models.CharField(
                        help_text="The variant being played as a string.", max_length=64
                    ),
                ),
                (
                    "num_players",
                    models.PositiveSmallIntegerField(
                        help_text="The number of players."
                    ),
                ),
                (
                    "deadline",
                    models.DateTimeField(help_text="The deadline to play this seed."),
                ),
            ],
            options={
                "ordering": ("-deadline",),
            },
        ),
        migrations.CreateModel(
            name="HanabiReplay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "replay_id",
                    models.PositiveIntegerField(
                        help_text="The ID of the replay.", unique=True
                    ),
                ),
                (
                    "game_score",
                    models.PositiveIntegerField(help_text="The game score."),
                ),
                (
                    "turn_count",
                    models.PositiveIntegerField(
                        help_text="The number of turns elapsed."
                    ),
                ),
                (
                    "spade_score",
                    models.FloatField(help_text="The number of spades obtained."),
                ),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hanabi.hanabicontest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HanabiPlayer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hanab_username",
                    models.CharField(
                        help_text="The username you use on hanab.live.",
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HanabiParticipation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hanabi.hanabiplayer",
                    ),
                ),
                (
                    "replay",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hanabi.hanabireplay",
                    ),
                ),
            ],
            options={
                "unique_together": {("player", "replay")},
            },
        ),
    ]
