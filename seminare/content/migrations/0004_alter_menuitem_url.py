# Generated by Django 5.1.4 on 2024-12-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0003_menugroup_menuitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="url",
            field=models.CharField(max_length=256),
        ),
    ]
