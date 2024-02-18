from django.contrib import admin
from .models import UserProfile,Experience,Education,Skills,UserSkills

# Register your models here.
admin.site.register((UserProfile,Experience,Education,Skills,UserSkills))
