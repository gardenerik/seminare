# Generated by Django 5.1.2 on 2024-12-08 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contests", "0002_category"),
        ("problems", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="problemset",
            name="contest",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contests.contest",
            ),
        ),
    ]
