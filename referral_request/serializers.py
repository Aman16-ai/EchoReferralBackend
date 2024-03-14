from rest_framework import serializers
from .models import ReferralRequest
from job.models import Job
from orgranisation.models import Organisations
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
        referralRequest = ReferralRequest(candidate = userProfile,**validated_data)
        referralRequest.save()
        return referralRequest


class GetReferralRequestModelSerialzer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = ReferralRequest
        # depth = 1