# Generated by Django 5.1.4 on 2024-12-10 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submits', '0003_alter_filesubmit_comment_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filesubmit',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='judgesubmit',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='textsubmit',
            options={'ordering': ['-created_at']},
        ),
    ]
