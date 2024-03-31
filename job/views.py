from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobModelSerializer,GetJobModelSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import docker
import subprocess
from .tasks import extract_and_add_skills
from django.conf import settings
from django_filters import rest_framework as filter
from rest_framework.decorators import action
from .service.JobService import JobService
# Create your views here.
class JobModelViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    # serializer_class = JobModelSerializer
    # permission_classes = [IsAuthenticated] currently anyone can add a job in future we will add permission so thtat only organistaions can perform CURD on jobs
    filter_backends = (filter.DjangoFilterBackend,)
    filterset_fields = ('organisation__name','organisation__id')
    serializers = {
        'list': GetJobModelSerialzer,
        'retrieve': GetJobModelSerialzer,
        'create':JobModelSerializer
    }

    @action(methods=['GET'],detail=False)
    def get_recent_jobs(self,request,pk=None):
        js = JobService()
        recent_jobs = js.recent_posted_jobs()
        print(recent_jobs)
        ser = self.serializers['list'](recent_jobs,many=True)
        
        return Response(ser.data)
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializers['list']
        elif self.action == 'retrieve':
            return self.serializers['retrieve']
        else:
            return self.serializers['create']
    def finalize_response(self, request, response, *args, **kwargs):
        final_response = Response(status=response.status_code,data={"status":response.status_code,"Response":response.data})
        final_response.accepted_renderer = request.accepted_renderer
        final_response.accepted_media_type = request.accepted_media_type
        final_response.renderer_context = self.get_renderer_context()
        return final_response
    
    def get_renderer_context(self):
        """
        Returns a dict that is passed through to Renderer.render(),
        as the `renderer_context` keyword argument.
        """
        # Note: Additionally 'response' will also be added to the context,
        #       by the Response object.
        return {
            'view': self,
            'args': getattr(self, 'args', ()),
            'kwargs': getattr(self, 'kwargs', {}),
            'request': getattr(self, 'request', None)
        }
    

@api_view(['GET'])
def testApi(request):
    client = docker.from_env()
    try:
        # command = ["docker", "run", "-i", "--rm", "skill-extractor-v2"]
        # process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        text = "Pursuing a bachelor's or master's degree in engineering, computer science or related field.Must have at least one additional quarter/semester of school remaining following the completion of the internship.One year of programming experience in an object-oriented language.Ability to demonstrate an understanding of computer science fundamentals, including data structures and algorithms"
        # stdout,stderr = process.communicate(text)

        # if process.returncode == 0:
        #     print('output',stdout)
        # else:
        #     print('error ',stderr)
        print(settings.SERVER_TYPE)
        result = extract_and_add_skills.delay(job_id=9)
        # if(settings.SERVER_TYPE != 'PROD'):
        #     print('cannot excute celery')
        # else:
        #     print(result)
    except Exception as e:
        print(e)
    return Response({'message':"running test api"})
