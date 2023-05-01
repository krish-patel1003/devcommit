# Generated by Django 4.2 on 2023-05-01 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0008_alter_submission_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.URLValidator(), django.core.validators.FileExtensionValidator(['jpeg', 'jpg', 'png', 'gif', 'pdf', 'docx', 'txt'])]),
        ),
    ]
