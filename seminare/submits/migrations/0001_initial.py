# Generated by Django 5.1.2 on 2024-12-03 15:24

import django.db.models.deletion
from django.db import migrations, models

import seminare.submits.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("problems", "0001_initial"),
        ("users", "0002_category_school_enrollment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Submit",
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
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("PR", "Program"),
                            ("DE", "Description"),
                            ("SU", "Susi"),
                        ]
                    ),
                ),
                ("score", models.FloatField(default=0)),
                ("graded", models.BooleanField()),
                ("protocol", models.TextField(blank=True)),
                (
                    "file",
                    models.FileField(
                        upload_to=seminare.submits.models.submit_file_file
                    ),
                ),
                (
                    "enrollment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.enrollment",
                    ),
                ),
                (
                    "problem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="problems.problem",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at", "score"],
            },
        ),
    ]
