from rest_framework import serializers
from .models import Job
from orgranisation.models import Organisations

class JobModelSerializer(serializers.ModelSerializer):
    organisation = serializers.PrimaryKeyRelatedField(queryset=Organisations.objects.all())

    class Meta:
        fields = "__all__"
        model = Job
        depth = 1