# Generated by Django 5.1.4 on 2024-12-15 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_trojsten_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.school'),
        ),
    ]
