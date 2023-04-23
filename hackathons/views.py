from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from hackathons.models import Hackathon
from hackathons.serializers import HackathonSerializer
from hackathons.permissions import IsOrganizationOrReadOnly
from hackathons.utils import convert_datetime_to_str
from datetime import datetime


CURRENT_DATETIME_STR = convert_datetime_to_str(datetime.now())

class HackathonViewSet(ModelViewSet):
    '''
    Hackathon viewset - handles POST, GET, PATCH, DELETE requests
    '''

    serializer_class = HackathonSerializer  
    queryset = Hackathon.objects.all()
    permission_classes = (IsAuthenticated, IsOrganizationOrReadOnly, )
    filterset_fields = ["title"]
    ordering_fields = ["start_datetime"]


    def create(self, request, *args, **kwargs):
        '''
        create method handles creating new hackathon
        '''

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(
                {"data": serializer.data, "message": "New Hackathon created!"}, 
                status=status.HTTP_201_CREATED
            )
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
           



    def update(self, request, *args, **kwargs):
        '''
        update method handles PATCH request of a hackathon
        '''

        data = request.data
        hackathon = self.get_object()
        start_datetime = convert_datetime_to_str(hackathon.start_datetime)
        end_datetime = convert_datetime_to_str(hackathon.end_datetime)

        if (CURRENT_DATETIME_STR >= start_datetime):

            return Response(
                {"error": "Hackathon has already started cannot edit now"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if (CURRENT_DATETIME_STR >= end_datetime):

            return Response(
                {"error": "Hackathon has already ended cannot edit now"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(instance=hackathon, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {"data": serializer.data, "message": "Hackathon details updated!"}, 
            status=status.HTTP_200_OK
        )
    

        
            








    
