from django.db import models
from accounts.models import User
from hackathons.models import Hackathon


class Enrollment(models.Model):
    '''
    Enrollment model - store user enrollments to hackathons
    '''

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon_id = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    registration_data = models.JSONField(default=dict)
    registration_datetime = models.DateTimeField(auto_now_add=True)
    submission_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user} - {self.hackathon.title}"
    


