# Generated by Django 4.2 on 2023-04-23 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='hackathon',
            new_name='hackathon_id',
        ),
    ]
