from account.models import UserProfile
from referral_request.models import ReferralRequest
from django.db.models import Count
class ReferralRequestService():

    def user_requests_status(self,user:UserProfile):
        requests = ReferralRequest.objects.filter(candidate=user).values('status').annotate(count=Count('status'))
        return requests