from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
        

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    projects = models.ManyToManyField(Project,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.client_name

