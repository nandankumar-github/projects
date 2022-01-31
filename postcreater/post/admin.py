from django.contrib import admin
from post.models import UserPost

# Register your models here.
@admin.register(UserPost)
class UserAdmin(admin.ModelAdmin):
    list_display=['who_post','name','comment']