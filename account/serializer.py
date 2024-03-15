from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import UserProfile,Experience
from orgranisation.models import Organisations
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
        currentOrgs = userService.getCurrentOrganisations()
        if(currentOrgs == None):
            response['curr_orgs'] = None
        else :
            exp_ser = GetUserExperienceSerializer(currentOrgs,many=True)
            response['curr_orgs'] = exp_ser.data
        print('user profile response to re',response['user'].pop('password'))
        return response
    class Meta:
        model = UserProfile
        fields = "__all__"



class UserExperienceSerializer(serializers.ModelSerializer):
    organisation = serializers.PrimaryKeyRelatedField(queryset=Organisations.objects.all())
    class Meta:
        exclude = ('userProfile',)
        model = Experience

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if self.context['request'].method == 'GET':
            response['userProfile'] = UserProfileSerializer(instance.userProfile).data
        return response
    def create(self, validated_data):
        try:
            user= self.context['request'].user
            userProfile = UserProfile.objects.get(user = user)
            if userProfile is not None:
                exp = userProfile.add_user_experience(data=validated_data)
                return exp
            raise ValidationError(detail={'Details':"User not found"})
        except Exception as e:
            print(e)
            raise ValidationError(detail={'Details':"Something went wrong"})
        

class GetUserExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Experience