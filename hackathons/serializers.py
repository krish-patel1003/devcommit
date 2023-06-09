from rest_framework import serializers
from hackathons.models import Hackathon
from datetime import datetime
from hackathons.utils import convert_datetime_to_str


class HackathonSerializer(serializers.ModelSerializer):
    '''
    Hackathon serializer
    '''


    username = serializers.CharField(source='organization.username',read_only=True)
    registration_deadline = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"])
    start_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"])
    end_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"])

    class Meta:
        model = Hackathon
        fields = (
            'id',
            'username', 
            'title', 
            'description', 
            'background_image', 
            'hackathon_image', 
            'type_of_submission',
            'registration_deadline',
            'start_datetime',
            'end_datetime',
            'reward_prize',
            'created_on'
        )
        extra_kwargs = {'created_on': {'read_only':True}}

    
    def validate(self, attrs):

        title = attrs.get('title', None)
        type_of_submission = attrs.get('type_of_submission', None)
        start_datetime = attrs.get('start_datetime', None)
        end_datetime = attrs.get('end_datetime', None)
        registration_deadline = attrs.get('registration_deadline', None)

        SUBMISSION_TYPES = ['IMG', 'LINK', 'FILE']

        if title and (not title.isalnum()):
            raise serializers.ValidationError("title should be alphanumeric")

        if type_of_submission and (type_of_submission not in SUBMISSION_TYPES):
            raise serializers.ValidationError(
                "Invalid Submission Type, submission type should be ['LINK', 'IMG', 'FILE'].")
        
        if start_datetime and end_datetime and start_datetime > end_datetime:
            raise serializers.ValidationError(
                "Invalid start_datetime and end_datetime. It should follow (end_datetime > start_datetime).")
        
        if start_datetime and convert_datetime_to_str(start_datetime) < convert_datetime_to_str(datetime.now()):
            raise serializers.ValidationError(
                "Invalid start_datetime, start_datetime cannot be before hackathon creation datetime.")

        if registration_deadline and (registration_deadline > start_datetime):
            raise serializers.ValidationError(
                "Invalid registration_deadline, registration date should be less then or equal to start_datetime")
        

        return attrs



            


        