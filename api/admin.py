from django.contrib import admin

from api.models import Client, Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name']
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
         obj.created_by = request.user
         obj.save()

  

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name','created_at']
    exclude = ['created_by']

    def save_model(self, request, obj,form, change):
         obj.created_by = request.user
         obj.save()

