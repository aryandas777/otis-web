# Generated by Django 4.1.10 on 2023-08-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0056_alter_userprofile_use_twemoji"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="show_portal_instructions",
            field=models.BooleanField(
                default=True,
                help_text="Show the instruction text above the units on the home page",
                verbose_name="Show portal instructions",
            ),
        ),
    ]