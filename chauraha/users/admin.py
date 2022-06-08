from django.contrib import admin
from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
  list_display = ['id', 'username', 'email', 'branch',]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['id', 'user',]
