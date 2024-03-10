from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from orgranisation.models import Organisations
# Create your models here.

    
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    headline = models.CharField(max_length=300)
    profile_completed = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.user.username
    def add_user_experience(self,data):
        experience = Experience(userProfile=self,**data)
        experience.save()
        return experience
    
    def get_all_experienceOfUser(self,countOnly):
        data = Experience.objects.filter(userProfile=self)
        print(data)
        if countOnly:
            return data.count()
        return data
    
    def add_user_education(self, data):
        education = Education(**data)
        education.save()
        return education

    def get_all_education_of_user(self,countOnly):
        data = Education.objects.filter(userProfile=self)
        if countOnly:
            return data.count()
        return data
    
    def add_user_skill(self,data):
        skill = UserSkills(self,**data)
        skill.save()
        return skill

    def get_user_skills(self,countOnly):
        data = UserSkills.objects.filter(userProfile=self)
        if countOnly:
            return data.count()
        return data
    
    

class Experience(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    userProfile = models.ForeignKey(UserProfile,on_delete= models.CASCADE)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.organisation.name}"
    
class Education(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    school = models.ForeignKey(Organisations, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    course_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.userProfile.user.username} - {self.course_name} at {self.school.name}"


class Skills(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=300)


    def save(self,*args,**kwargs):
        self.name = self.name.lower()
        super(Skills,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name
    
class UserSkills(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE)