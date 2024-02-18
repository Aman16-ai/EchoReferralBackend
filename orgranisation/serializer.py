from .models import Organisations
from rest_framework import serializers

class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        fields="__all__"
        model=Organisations