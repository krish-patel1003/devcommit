from django.db import models
from accounts.models import User
from hackathons.models import Hackathon


class Enrollment(models.Model):
    '''
    Enrollment model - store user enrollments to hackathons
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    registration_data = models.JSONField(default=dict, null=True)
    registration_datetime = models.DateTimeField(auto_now_add=True)
    submission_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user} - {self.hackathon.title}"
    


