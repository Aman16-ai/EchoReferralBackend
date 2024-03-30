from rest_framework import serializers
from .models import Job
from orgranisation.models import Organisations
from .tasks import extract_and_add_skills
from django.conf import settings
from .service.JobService import JobService
class JobModelSerializer(serializers.ModelSerializer):
    organisation = serializers.PrimaryKeyRelatedField(queryset=Organisations.objects.all())

    class Meta:
        fields = "__all__"
        model = Job
        depth = 1

    def create(self, validated_data):
        # Migrate this code in Jobservice class
        job = Job(**validated_data)
        job.save()

        # As we have free prodcution server so we cannot use shell to run celery in production
        if(settings.SERVER_TYPE == 'DEV'): 
            extract_and_add_skills.delay(job.id)

        else:
            service = JobService()
            service.extract_and_add_skills(job)
        return job

class GetJobModelSerialzer(serializers.ModelSerializer):

    def to_representation(self, instance:Job):
        response = super().to_representation(instance)
        skills = instance.get_all_skills(fullObject=False)
        print(list(skills))
        response['skills'] = list(skills)
        return response
    class Meta:
        fields = "__all__"
        model = Job
        depth = 1