from job.models import  JobSkill
from account.models import Skills
from job.models import Job
from .skillsExtractor import SkillsExtractor
import ast
import datetime
from django.utils import timezone
from django.db.models import Q
class JobService:

    def extract_and_add_skills(self,job:Job):
        text = job.qualifications + job.requirements
        skill_extractor = SkillsExtractor(text)
        skills_result = skill_extractor.extract()
        skills_lst = ast.literal_eval(skills_result)
        for skill in skills_lst:
            job.add_skills(skill_name=skill)


    def recent_posted_jobs(self):
        try:
            print(timezone.now())
            current_date = datetime.datetime.now().date()
            last_week_date = current_date - datetime.timedelta(days=7)
            recent_jobs = Job.objects.filter(Q(post_date__gte=last_week_date) & Q(post_date__lte=current_date))
            print(recent_jobs)
            return recent_jobs
        except Exception as e:
            print(e)
            return None