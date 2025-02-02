from rest_framework import serializers
#from .models import *
from politician.models import Community, Board, Quiz, Opinion

class CommunitySerializer(serializers.ModelSerializer):
    formatted_created_at = serializers.DateTimeField(source='created_at', format='%Y.%m.%d, %H:%M:%S', read_only=False)
    formatted_deadline = serializers.DateTimeField(source='deadline', format='%Y.%m.%d, %H:%M:%S', read_only=False)


    class Meta:
        model = Community
        #fields = '__all__'
        fields = ('community_id','title', 'content', 'formatted_created_at', 'formatted_deadline')


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'
  

class OpinionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opinion
        fields = '__all__'
     

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'
