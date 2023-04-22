from django.db import models
from accounts.models import User
from hackathons.utils import hackathon_image_path
import os


class Hackathon(models.Model):
    '''
    Hackathon model 
    '''

    SUBMISSION_TYPES = [
        ('IMG', 'Image'),
        ('FILE', 'File'),
        ('LINK', 'Link')
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(blank=True)
    background_image = models.ImageField(
        default='default/no_image.jpg', upload_to=hackathon_image_path(image_type="bg"), max_length=255)
    hackathon_image = models.ImageField(
        default='default/no_image.jpg', upload_to=hackathon_image_path(image_type="hack"), max_length=255)
    type_of_submission = models.CharField(choices=SUBMISSION_TYPES, max_length=4, default="LINK")
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)
    reward_prize = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




