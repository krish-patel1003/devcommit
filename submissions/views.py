from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from enrollments.models import Enrollment
from submissions.models import Submission
from submissions.serializers import SubmissionSerializer
from submissions.permissions import IsUserOwnerOrReadOnly


class SubmissionViewSet(ModelViewSet):
    '''
    Submission view set - handles POST, GET, PATCH, DELETE requests for submissions
    '''

    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
    permission_classes = (IsAuthenticated, IsUserOwnerOrReadOnly)


    def list(self, request, *args, **kwargs):
        
        user = request.user
        if user.is_organization:
            queryset = self.queryset.filter(hackathon_id__user_id=user).order_by('-submission_datetime')
        else:
            queryset = self.queryset.filter(user_id=user).order_by('-submission_datetime')
        serializer = self.serializer_class(queryset, many=True)

        return Response(
            {"data": serializer.data, "message": "List of all the submissions to hackathon"}, 
            status=status.HTTP_200_OK
        )


    def create(self, request, *args, **kwargs):
        '''
        create method handles submission to a hackathon
        '''

        data = request.data
        user = request.user
        serializer = self.serializer_class(data=data)
       
        if serializer.is_valid():

            if not Enrollment.objects.filter(user_id=user, hackathon_id=data['hackathon_id']).exists():
                return Response(
                    {"error": "Logged in user is not enrolled to the hackathon, cannot submit without enrollment"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            if Submission.objects.filter(user_id=user, hackathon_id=data['hackathon_id']).exists():
                return Response(
                    {"error": "You have already made the submission, cannot create new"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            enrollment = Enrollment.objects.get(user_id=user, hackathon_id=data['hackathon_id'])

            serializer.save(user_id=user, enrollment_id=enrollment)

            enrollment.submission_status = True
            enrollment.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": f"enrolled to hackathon, {serializer.data['hackathon']}"
                }, 
                status=status.HTTP_201_CREATED
            )
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
