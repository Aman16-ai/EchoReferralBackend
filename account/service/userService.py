from account.models import UserProfile
class UserService:

    def __init__(self,user) -> None:
        # self.user = user
        self.userProfile:UserProfile = user

    def getProfileCompletedProgress(self):
        exp_count = self.userProfile.get_all_experienceOfUser(countOnly=True)
        edu_count = self.userProfile.get_all_education_of_user(countOnly=True)
        skills_count = self.userProfile.get_user_skills(countOnly=True)
        headline_added = 0
        if self.userProfile.headline not in ['',' ']:
            headline_added = 1
        if exp_count > 0:
            exp_count = 1
        if edu_count > 0:
            exp_count = 1
        if skills_count > 0:
            skills_count = 1

        print(exp_count,edu_count,skills_count,headline_added)
        progress = ((exp_count + edu_count + skills_count + headline_added) / 4) * 100
        return progress
    
    def getCurrentOrganisations(self):
        allExperiences = self.userProfile.get_all_experienceOfUser(countOnly=False)
        if len(allExperiences) == 0:
            return None
        else : 
            return allExperiences.filter(end_date=None)