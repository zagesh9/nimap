from django.contrib import admin
from django.urls import path,include
from api.views import ClientViewSet,ProjectViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [    
    path('',include(router.urls))
]