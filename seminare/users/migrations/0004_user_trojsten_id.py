# Generated by Django 5.1.4 on 2024-12-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_enrollment_grade"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="trojsten_id",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
