# Generated by Django 4.2 on 2023-04-22 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackathons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_data', models.JSONField(default=dict)),
                ('registration_datetime', models.DateTimeField(auto_now_add=True)),
                ('submission_status', models.BooleanField(default=False)),
                ('hackathon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathons.hackathon')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
