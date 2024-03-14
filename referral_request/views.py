from django.shortcuts import render
from .serializers import ReferralRequestModelSerialzer,GetReferralRequestModelSerialzer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import ReferralRequest
from rest_framework.response import Response
from middleware.custom_permission import IsAdminOrReferralRequestOwner
# Create your views here.

class ReferralRequestModelViewSet(viewsets.ModelViewSet):
    queryset = ReferralRequest.objects.all()
    permission_classes = [IsAuthenticated,IsAdminOrReferralRequestOwner]
    serializer_class = ReferralRequestModelSerialzer

    serializers = {
        'list' : GetReferralRequestModelSerialzer,
        'create' : ReferralRequest,
        'retrieve':GetReferralRequestModelSerialzer
    }


    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.serializers['list']
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
    
