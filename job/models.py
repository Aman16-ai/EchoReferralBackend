from django.db import models
from orgranisation.models import Organisations
from account.models import Skills
# Create your models here.

employmentType = (
    ('Full Time','Full Time'),
    ('Internship','Internship'),
    ('Contract','Contract')
)
DisciplineType = (
    ("Software Engineering","Software Engineering"),
)
class Job(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    job_number = models.CharField(max_length=250,null=True,blank=True)
    post_date = models.DateField()
    title = models.CharField(max_length=150)
    organisation = models.ForeignKey(Organisations,on_delete=models.CASCADE)
    link = models.TextField(null=True,blank=True)
    employment_type = models.CharField(max_length=50,choices=employmentType)
    Discipline = models.CharField(max_length=150,choices=DisciplineType)
    description = models.TextField()
    qualifications = models.TextField()
    requirements = models.TextField(null=True,blank=True)

    def get_all_skills(self,fullObject):
        if fullObject != True:
            return JobSkill.objects.filter(job=self).values_list("skill__name",flat=True)
        return JobSkill.objects.filter(job=self)
    
    def add_skills(self,skill_name):
        skill = Skills(name=skill_name)
        skill.save()
        job_skill = JobSkill(job=self,skill=skill)
        job_skill.save()

    def __str__(self) -> str:
        return self.title + " at " + self.organisation.name
    

class JobSkill(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.job.title + " " + self.skill.name