from celery import shared_task
import subprocess

@shared_task(bind=True)
def extract_and_add_skills(self,text):
    try:
        command = ["docker", "run", "-i", "--rm", "skill-extractor-v2"]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        text = "Pursuing a bachelor's or master's degree in engineering, computer science or related field.Must have at least one additional quarter/semester of school remaining following the completion of the internship.One year of programming experience in an object-oriented language.Ability to demonstrate an understanding of computer science fundamentals, including data structures and algorithms"
        stdout,stderr = process.communicate(text)

        if process.returncode == 0:
            print('output',stdout)
        else:
            print('error ',stderr)
    except Exception as e:
        print(e)