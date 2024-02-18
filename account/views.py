from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile
from .serializer import UserSerializer,LoginSerializer
from utils.tokenUtils import get_tokens_for_user
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework import status
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    @action(detail=False,methods=['POST'])
    def login(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            user = authenticate(username=data['username'],password=data['password'])
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(token)
            else:
                return Response({"User not found"})
        else:
            return Response(serializer.error_messages)

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