from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractBaseUser):
    '''
    Custom AUTH_USER_MODEL.
    '''

    username = models.CharField(max_length=255, unique=True, null=False, db_index=True)
    email = models.EmailField(max_length=255, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=255)
    is_organization = models.BooleanField(default=False)

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = UserManager()

    def __str__(self):
        '''
        returns a string - "<username>."
        '''
        
        return self.username
    
    def tokens(self):
        '''
        returns a object - containing refresh_token and access_token.
        '''

        refresh_token = RefreshToken.for_user(self)
        return {
            'refresh_token':str(refresh_token),
            'access_token':str(refresh_token.access_token)
        }


