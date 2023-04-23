from rest_framework import serializers
from hackathons.models import Hackathon
from submissions.models import Submission
from datetime import datetime
from hackathons.utils import convert_datetime_to_str


class SubmissionSerializer(serializers.ModelSerializer):
    '''
    Submission serializer
    '''

    username = serializers.CharField(source='user_id.username',read_only=True)
    hackathon = serializers.CharField(source='hackathon_id.title',read_only=True)


    class Meta:
        model = Submission
        fields = (
            'id',
            'username',
            'hackathon',
            'hackathon_id',
            'enrollment_id',
            'project_name',
            'summary',
            'type_of_submission',
            'image_submission',
            'file_submission',
            'link_submission',
            'submission_datetime',
            'is_favourite'
        )
        extra_kwargs = {
            'type_of_submission': {'read_only':True},
            'submission_datetime': {'read_only':True},
            'enrollment_id': {'read_only': True}
        }


    def validate(self, attrs):

        type_of_submission = attrs.get('type_of_submission', None)
        image_submission = attrs.get('image_submission', None)
        file_submission = attrs.get('file_submission', None)
        link_submission = attrs.get('link_submission', None)

        if type_of_submission:
            if type_of_submission == "LINK":
                if image_submission or file_submission:
                    raise serializers.ValidationError("Type of submission is LINK, image and file not allowed")
            
            if type_of_submission == "FILE":
                if image_submission or link_submission:
                    raise serializers.ValidationError("Type of submission is FILE, image and link not allowed")
            
            if type_of_submission == "IMG":
                if image_submission or file_submission:
                    raise serializers.ValidationError("Type of  is IMG, link and file not allowed")

        else:
            raise serializers.ValidationError("type_of_submission, not rendered")   
        
        return attrs


                
    def create(self, validated_data):

        hackathon = Hackathon.objects.get(id=validated_data['hackathon_id'])
        start_datetime = hackathon.start_datetime
        end_datetime = hackathon.end_datetime
        submission_datetime = validated_data['submission_datetime']

        if submission_datetime > end_datetime:
            raise serializers.ValidationError(
                "Hackathon has ended, new submission cannot be made.")
        
        if submission_datetime < start_datetime:
            raise serializers.ValidationError(
                "Hackathon has not started yet, new submission cannot be made.")

        return super().create(validated_data)
    




        