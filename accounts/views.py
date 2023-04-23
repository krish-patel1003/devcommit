from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from accounts.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(GenericAPIView):
    '''
    Register View - handles user registration
    '''

    serializer_class = RegisterSerializer
    authentication_classes = []

    def post(self, request):

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if request.data.get('is_organization', False):
            return Response(
                {"data": serializer.data, "msg":"new organization registered"}, status=status.HTTP_201_CREATED)

        return Response(
            {"data": serializer.data, "mssg": "new user registerd"}, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    '''
    Login View - handles login
    '''
        
    serializer_class = LoginSerializer
    authentication_classes = []

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(
            {"data": serializer.data, "mssg": "user logged in"}, status=status.HTTP_200_OK)

