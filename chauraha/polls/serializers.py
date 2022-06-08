
from .models import Poll, Choice, Vote
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from users.serializers import CustomUserSerializer


class VoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vote
        fields = ('id', 'poll', 'choice', 'user',)
        read_only_fields = ('user', )

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Choice
        fields = ('id', 'poll', 'choice_text', 'votes' )
        read_only_fields = ('poll', )

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = ('id', 'text','owner',  'pub_date', 'active', 'choices')
        read_only_fields = ('owner', 'active', 'pub_date',)




