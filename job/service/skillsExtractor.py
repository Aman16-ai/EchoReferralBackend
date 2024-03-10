import subprocess
class SkillsExtractor():

    def __init__(self,text,docker_image="amandev7531/echo-skill-extractor:v2.0") -> None:
        self.doc = text
        self.command = ["docker", "run", "-i", "--rm", docker_image]


    def extract(self):
        process = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout,stderr = process.communicate(self.doc)
        if process.returncode == 0:
           return stdout
        else:
            raise RuntimeError(stderr)
