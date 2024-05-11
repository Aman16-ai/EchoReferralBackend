from rest_framework import serializers
from .models import ReferralRequest
from job.models import Job
from orgranisation.models import Organisations
from .service.CandidateScoreService import CandidateScoreService
from account.models import UserProfile

class ReferralRequestModelSerialzer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all()) 
    organisation = serializers.PrimaryKeyRelatedField(queryset=Organisations.objects.all())
    class Meta:
        exclude = ("candidate","score")
        model = ReferralRequest
        depth = 1
    
    def create(self, validated_data):
        user = self.context['request'].user
        userProfile = UserProfile.objects.get(user=user)
        pitch = validated_data.get('pitch')
        job:Job = validated_data.get('job')
        print('user pitch',pitch)
        print('user job',job)

        # this task will be execute through celery
        cs = CandidateScoreService()
        score = cs.get_score(jd = job.description,pitch=pitch)
        referralRequest = ReferralRequest(candidate = userProfile,score=score,**validated_data)
        referralRequest.save()
        return referralRequest


class GetReferralRequestModelSerialzer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = ReferralRequest
        # depth = 1