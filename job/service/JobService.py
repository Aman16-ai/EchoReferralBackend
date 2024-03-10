from job.models import  JobSkill
from account.models import Skills
from job.models import Job
from .skillsExtractor import SkillsExtractor
import ast
class JobService:

    def extract_and_add_skills(self,job:Job):
        text = job.qualifications + job.requirements
        skill_extractor = SkillsExtractor(text)
        skills_result = skill_extractor.extract()
        skills_lst = ast.literal_eval(skills_result)
        for skill in skills_lst:
            job.add_skills(skill_name=skill)
