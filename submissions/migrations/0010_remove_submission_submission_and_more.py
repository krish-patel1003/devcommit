# Generated by Django 4.2 on 2023-05-02 16:36

from django.db import migrations, models
import submissions.models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0009_alter_submission_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submission',
        ),
        migrations.AddField(
            model_name='submission',
            name='file_submission',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=submissions.models.submission_path),
        ),
        migrations.AddField(
            model_name='submission',
            name='link_submission',
            field=models.URLField(blank=True, null=True),
        ),
    ]