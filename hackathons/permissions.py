from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import User


class IsOrganizationOrReadOnly(BasePermission):
    '''
    IsOrganization permission will check whether,
    the user performing a particular action is a Organization or not
    '''

    message = "User if only create, update, or delete a hackathon, if it is a organization"

    def has_permission(self, request, view):
        
        if request.method == "POST":
            print("checking post request perm")
            if not request.user.is_organization:
                self.message = "Logged in user is not a organization"
                return False
            
            if "username" in list(request.data.keys()):
                if not request.user.username == request.data['username']:
                    self.message = "Logged in user and input user do not match"
                    return True
                else:
                    return False
            
            return request.user.is_organization
        
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_organization

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        if request in ["PUT", "PATCH", "DELETE"]:
            return obj.user_id == request.user

        return False
        

        
        
