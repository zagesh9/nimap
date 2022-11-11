from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset= Client.objects.all()
    serializer_class=ClientSerializer
    

    @action(detail=True,methods=['get'])
    def projects(self,request,pk=None):   
        try:                
            client=Client.objects.get(pk=pk)
            proj=Project.objects.filter(client=client)
            proj_serializer = ProjectSerializer(proj,many=True)
            return Response(proj_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Client might not exists !! Error'
            })


class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer