from django.db import models
from accounts.models import User
from hackathons.models import Hackathon
from enrollments.models import Enrollment
from submissions.utils import hackathon_submission_image_path


class Submission(models.Model):
    '''
    Submission model - it will store Hackathon subimssions
    '''

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon_id = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255, null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
    type_of_submission = models.CharField(default='LINK', max_length=4, null=False, blank=False)
    image_submission = models.ImageField(
        upload_to=hackathon_submission_image_path("image"), max_length=255, null=True, blank=False)
    file_submission = models.FileField(
        upload_to=hackathon_submission_image_path("file"), max_length=255, null=True, blank=False)
    link_submission = models.URLField(null=True, blank=False)
    submission_datetime = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} - {self.hackathon.title} - {self.project_name}"
    
    



