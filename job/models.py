from django.db import models
from orgranisation.models import Organisations
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


    def __str__(self) -> str:
        return self.title + "at" + self.organisation.name