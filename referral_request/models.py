from django.db import models
from orgranisation.models import Organisations
from account.models import UserProfile
from job.models import Job

request_status = (
    ('send','send'),
    ('received','received'),
    ('approved','approved'),
    ('rejected','rejected')
)
class ReferralRequest(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    organisation = models.ForeignKey(Organisations,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    candidate = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    pitch = models.TextField()
    status = models.CharField(choices=request_status,null=True,blank=True,default='send',max_length=10)
    score = models.FloatField(null=True,blank=True,default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.candidate.user.username + " " + self.job.title + " at " + self.organisation.name