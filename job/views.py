from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobModelSerializer
from rest_framework.response import Response
# Create your views here.
class JobModelViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobModelSerializer
    # permission_classes = [IsAuthenticated] currently anyone can add a job in future we will add permission so thtat only organistaions can perform CURD on jobs

    
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