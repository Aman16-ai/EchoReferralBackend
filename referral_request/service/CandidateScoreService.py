import requests

class CandidateScoreService:
    

    def __init__(self) -> None:
        self.base_url = "https://echoreferral-nlp-latest.onrender.com/"
    
    def get_score(self,jd:str,pitch:str):
        payload = {
            'candidate_descriptions' : [pitch],
            'job_description' : jd
        }
        response = requests.post(f"{self.base_url}calculateRank/",json=payload)
        score = response.json()['Response'][0]['score']
        rounded_score = round(score*100,2)
        return rounded_score
        