from rest_framework.permissions import BasePermission, SAFE_METHODS
from enrollments.models import Enrollment
from accounts.models import User
from hackathons.models import Hackathon


class EnrollmentPermissions(BasePermission):
    '''
    Enrollment permissions - It will allow normal users to enroll for a hackathon, 
    and organizers see all the enrollments
    '''

    message = "Only normal users can enroll to a hackathon, and the organizers can see all the enrollments"
    
    def has_permission(self, request, view):
        
        if request.method == "POST":
            if request.user.is_organization:
                self.message = "You are organization, you cannot enroll to a hackathon"
                return False
            else:
                return True
            
        return True
    

    def has_object_permission(self, request, view, obj):
        
        if view.action in ['partial_update', 'update']:
            self.message = "Once enrolled, enrollment cannot be edited"
            return False
        
        if view.action in ['retrieve', 'destroy']:
            self.message = "You should be enrolled user, or the hackathon organizer to permform this action."
            return request.user == obj.user or request.user == obj.hackathon.organization
        
        if view.action in ['list']:
            return True
        
        return True
        

        
        

