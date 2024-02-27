from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import UserProfile
from .service.userService import UserService
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ("id","first_name","last_name","username","password","email")
        model = User

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     if self.context['request'].method == 'GET':
    #         response.pop('password')
    #     return response
    
    def create(self, validated_data):
        try:
            first_name = validated_data.pop('first_name')
            last_name = validated_data.pop('last_name')
            userobj =  User.objects.create_user(**validated_data)
            userobj.first_name = first_name
            userobj.last_name = last_name
            userobj.save()

            #init user profile
            if userobj is not None:
                user_profile = UserProfile(user=userobj,headline="")
                user_profile.save()
            
            return userobj
            
        except Exception as e:
            print(e)
            raise ValidationError(detail={"Details":"Something went wrong"})
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def to_representation(self, instance):
        response = super().to_representation(instance)
        userService = UserService(instance)
        progress = userService.getProfileCompletedProgress()
        response['profile_progress'] = progress
        print('user profile response to re',response['user'].pop('password'))
        return response
    class Meta:
        model = UserProfile
        fields = "__all__"