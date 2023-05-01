from rest_framework import serializers

from hackathons.models import Hackathon
from submissions.models import Submission
from datetime import datetime
from hackathons.utils import convert_datetime_to_str
from submissions.utils import hackathon_submission_image_path

IMG_SUBMISSION_PATH = hackathon_submission_image_path("image")
FILE_SUBMISSION_PATH = hackathon_submission_image_path("file")


class SubmissionSerializer(serializers.ModelSerializer):
    '''
    Submission serializer
    '''

    username = serializers.CharField(source='user.username',read_only=True)
    hackathon_title = serializers.CharField(source='hackathon.title',read_only=True)


    class Meta:
        model = Submission
        fields = (
            'id',
            'username',
            'hackathon_title',
            'hackathon',
            'enrollment',
            'project_name',
            'summary',
            'submission_type',
            'submission',
            'submission_datetime',
            'is_favourite'
        )
        extra_kwargs = {
            'submission_type': {'read_only':True},
            'submission_datetime': {'read_only':True},
            'enrollment': {'read_only': True}
        }
    
      
    def create(self, validated_data):
        print(validated_data)
        hackathon = validated_data['hackathon']
        start_datetime = convert_datetime_to_str(hackathon.start_datetime)
        end_datetime = convert_datetime_to_str(hackathon.end_datetime)
        current_datetime_str = convert_datetime_to_str(datetime.now())

        type_of_submission = hackathon.type_of_submission
        validated_data['type_of_submission'] = type_of_submission

        if current_datetime_str > end_datetime:
            raise serializers.ValidationError(
                "Hackathon has ended, new submission cannot be made.")
        
        if current_datetime_str < start_datetime:
            raise serializers.ValidationError(
                "Hackathon has not started yet, new submission cannot be made.")

        return super().create(validated_data)
    




        