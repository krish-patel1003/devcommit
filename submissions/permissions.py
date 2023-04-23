from rest_framework.permissions import BasePermission


class IsUserOwnerOrReadOnly(BasePermission):
    '''
    IsUserOwnerOrReadOnly permission class handles request from users,
    only allow enrolled user to submit to a hackathon and the organizations
    view the submission.
    '''

    message = ""

    def has_permission(self, request, view):
        
        if view.action in ["create"]:

            if request.user.is_organization:
                self.message = "A organization cannot make a submission"
                return False
            
            else:
                if "username" in list(request.data.keys()):
                    if not (request.user.username == request.data['username']):
                        self.message = "Logged in user and input user do not match"
                        return False
                    else:
                        return True
                
                return True
        
        return True


    def has_object_permission(self, request, view, obj):
       
        if view.action in ['destroy', 'partial_update', 'update']:
            self.message = "user should be the submission owner to edit it."
            return request.user == obj.user_id
        
        if view.action in ['retrieve', 'list']: 
            return True
        
        return True    
            
