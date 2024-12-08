# Generated by Django 5.1.2 on 2024-12-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_enrollment_category_delete_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enrollment",
            name="grade",
            field=models.CharField(
                choices=[
                    ("5ZS", "5zš"),
                    ("6ZS", "6zš"),
                    ("7ZS", "7zš"),
                    ("8ZS", "8zš"),
                    ("9ZS", "9zš"),
                    ("1SS", "1"),
                    ("2SS", "2"),
                    ("3SS", "3"),
                    ("4SS", "4"),
                    ("5SS", "5"),
                    ("OLD", "∞"),
                ],
                max_length=3,
            ),
        ),
    ]
