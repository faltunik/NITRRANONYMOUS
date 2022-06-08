from django.contrib import admin
from .models import Poll, Choice, Vote

# Register your models here.
@admin.register(Poll)
class CustomPollAdmin(admin.ModelAdmin):
  list_display = ['id', 'text', ]

@admin.register(Choice)
class CustomChoiceAdmin(admin.ModelAdmin):
  list_display = ['id', 'choice_text', ]

@admin.register(Vote)
class CustomVoteAdmin(admin.ModelAdmin):
  list_display = ['id', 'poll', 'choice', 'user', ]
