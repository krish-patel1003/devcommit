# Generated by Django 4.2 on 2023-04-28 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0002_alter_enrollment_registration_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='hackathon_id',
            new_name='hackathon',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user_id',
            new_name='user',
        ),
    ]
