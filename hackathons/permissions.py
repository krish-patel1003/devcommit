from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrganizationOrReadOnly(BasePermission):
    '''
    IsOrganization permission will check whether,
    the user performing a particular action is a Organization or not
    '''

    message = "User can only create, update, or delete a hackathon, if it is a organization"

    def has_permission(self, request, view):
        
        if view.action in ["create"]:

            if not request.user.is_organization:
                self.message = "Logged in user is not an organization"
                return False
            
            if "username" in list(request.data.keys()):
                if not (request.user.username == request.data['username']):
                    self.message = "Logged in user and input user do not match"
                    return False
                else:
                    return True
                
            return True
        
        return True
    

    def has_object_permission(self, request, view, obj):
        
        if view.action in ["partial_update", "update", "destroy"]:
            self.message = "Logged in user is not the Hackathon organizer"
            return obj.organization == request.user

        if view.action in ["list", "retrieve"]:
            return True
        
        return False
        

        
        
