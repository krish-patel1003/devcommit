from rest_framework import serializers
from enrollments.models import Enrollment
from datetime import datetime
from hackathons.utils import convert_datetime_to_str


class EnrollmentSerializer(serializers.ModelSerializer):
    '''
    Enrollment serializer 
    '''

    username = serializers.CharField(source='user.username',read_only=True)
    hackathon_title = serializers.CharField(source='hackathon.title',read_only=True)
    registration_data = serializers.JSONField()

    class Meta:
        model = Enrollment
        fields = (
            'id',
            'username',
            'hackathon',
            'hackathon_title',
            'registration_data',
            'registration_datetime',
            'submission_status'
        )
        extra_kwargs = { 
            'submission_status': {'read_only':True}
        }

    def create(self, validated_data):
        
        hackathon = validated_data['hackathon']
        registration_deadline = hackathon.registration_deadline

        if convert_datetime_to_str(registration_deadline) < convert_datetime_to_str(datetime.now()):
            serializers.ValidationError("Registration deadline has passed, cannot enroll now.")

        return super().create(validated_data)
    