# Generated by Django 4.2.5 on 2023-11-01 10:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exams", "0032_alter_practiceexam_url1_alter_practiceexam_url2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mockcompleted",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]