# Generated by Django 5.1.4 on 2024-12-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_alter_problem_problem_set_alter_text_problem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemset',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name='text',
            constraint=models.UniqueConstraint(models.F('problem'), models.F('type'), name='text__unique_problem_type'),
        ),
    ]