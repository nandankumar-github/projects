import imp
from django.contrib import admin
from blog.models import AdmissionModel

# Register your models here.
@admin.register(AdmissionModel)
class AdminssionAdmin(admin.ModelAdmin):
    list_display=['admission_though','name','roll','address']
