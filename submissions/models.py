from typing import Collection, Optional
from django.db import models
from django.db.models import FileField, ImageField, URLField
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, URLValidator
from accounts.models import User
from hackathons.models import Hackathon
from enrollments.models import Enrollment
from submissions.utils import hackathon_submission_image_path
import os

IMG_SUBMISSION_PATH = hackathon_submission_image_path("image")
FILE_SUBMISSION_PATH = hackathon_submission_image_path("file")

def submission_path(instance, filename):
        file_path = os.path.join(f"hackathon_submission/{instance.submission_type}", filename)
        return file_path


class Submission(models.Model):
    '''
    Submission model - it will store Hackathon subimssions
    '''

    SUBMISSION_TYPE_VALIDATORS = {
        'image': FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'gif']),
        'file': FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'txt']),
        'link': URLValidator(),
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255, null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
    submission_type = models.CharField(default='LINK', max_length=4, null=False, blank=False)
    submission = models.CharField(
         max_length=255, validators=[URLValidator(), FileExtensionValidator(['jpeg', 'jpg', 'png', 'gif', 'pdf', 'docx', 'txt'])], null=True, blank=True)
    submission_datetime = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.hackathon.title} - {self.project_name}"
    
    def clean(self):
        print("clean method called")
        super().clean()
        self.submission_type = self.hackathon.type_of_submission
        validator = self.SUBMISSION_TYPE_VALIDATORS.get(self.submission_type)
        if validator:
            try:
                validator(self.submission)
            except ValidationError as e:
                raise ValidationError({'submission_data': e})
        else:
            raise ValidationError({'submission_type': 'Invalid submission type'})

    



