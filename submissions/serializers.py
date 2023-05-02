from rest_framework import serializers
from django.core.validators import FileExtensionValidator, URLValidator
from hackathons.models import Hackathon
from submissions.models import Submission
from datetime import datetime
from hackathons.utils import convert_datetime_to_str


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
            'file_submission',
            'link_submission',
            'submission_datetime',
            'is_favourite'
        )
        extra_kwargs = {
            'submission_type': {'read_only':True},
            'submission_datetime': {'read_only':True},
            'enrollment': {'read_only': True}
        }
    

    def validate_file_submission_type(self, submission_type, data):
        print("submission clean method working?")
        print(data)

        if not submission_type:
            raise serializers.ValidationError('Submission type is required')

        if not data.get("file_submission"):
            raise serializers.ValidationError('File Submission is required')

        validators = {
            'FILE': FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'txt']),
            'IMG': FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])
        }

        validator = validators.get(submission_type)
        print(validator)
        if validator is None:
            raise serializers.ValidationError('Invalid submission type')

        try:
            validator(data.get("file_submission"))
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'submission': e})
        
        return True
    
    def validate(self, attrs):
        print(attrs.get("hackathon").type_of_submission)
        attrs["submission_type"] = attrs.get("hackathon").type_of_submission
        submission_type = attrs.get("submission_type")
        link_submission = attrs.get("link_submission")
        file_submission = attrs.get("file_submission")

        if not submission_type == "LINK":
            if not self.validate_file_submission_type(submission_type, attrs) or link_submission:
                raise serializers.ValidationError("Invalid submission type (validate method failed)")
        else:
            if not link_submission or file_submission:
                raise serializers.ValidationError("Link submission type allowed (validate method failed)")

        return super().validate(attrs)
      
    def create(self, validated_data):
        print(validated_data)
        hackathon = validated_data['hackathon']
        start_datetime = convert_datetime_to_str(hackathon.start_datetime)
        end_datetime = convert_datetime_to_str(hackathon.end_datetime)
        current_datetime_str = convert_datetime_to_str(datetime.now())


        if current_datetime_str > end_datetime:
            raise serializers.ValidationError(
                "Hackathon has ended, new submission cannot be made.")
        
        if current_datetime_str < start_datetime:
            raise serializers.ValidationError(
                "Hackathon has not started yet, new submission cannot be made.")


        return super().create(validated_data)
    




        