from rest_framework import serializers
from enrollments.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    '''
    Enrollment serializer 
    '''

    username = serializers.CharField(source='user_id.username',read_only=True)
    hackathon = serializers.CharField(source='hackathon_id.title',read_only=True)
    registration_data = serializers.JSONField()

    class Meta:
        model = Enrollment
        fields = (
            'id',
            'username',
            'hackathon_id',
            'hackathon',
            'registration_data',
            'registration_datetime',
            'submission_status'
        )
        extra_kwargs = { 
            'submission_status': {'read_only':True}
        }

    