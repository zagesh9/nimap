from rest_framework import serializers
from api.models import *
from django.forms import ValidationError

#create serializers here

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=100)


                
class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    created_by = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')
    class Meta:  
        model = Project
        fields=['project_name','created_by','user']
    

class ClientSerializer(serializers.ModelSerializer):
    client_id=serializers.ReadOnlyField()
    created_by = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')
    projects = ProjectSerializer(many=True)
    class Meta:
        model = Client
        fields="__all__"


