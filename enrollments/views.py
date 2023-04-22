from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from enrollments.models import Enrollment
from enrollments.serializers import EnrollmentSerializer
from enrollments.permissions import EnrollmentPermissions


class EnrollmentViewSet(ModelViewSet):
    '''
    Enrollment viewset handles POST, 
    '''

    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = (IsAuthenticated, EnrollmentPermissions)

    def create(self, request, *args, **kwargs):
        '''
        create method handles enrollment to a hackathon
        '''

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(
                {
                    "data": serializer.data, 
                    "message": f"enrolled to hackathon, {serializer.data['hackathon']}"
                }, 
                status=status.HTTP_201_CREATED
            )
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        
        user = request.user
        if user.is_organization:
            queryset = self.queryset.filter(hackathon_id__user_id=user).order_by('-registration_datetime')
        else:
            queryset = self.queryset.filter(user_id=user).order_by('-registration_datetime')
        serializer = self.serializer_class(queryset, many=True)

        return Response(
            {"data": serializer.data, "message": "List of all the enrollment to the hackathons"}, 
            status=status.HTTP_200_OK
        )

    
