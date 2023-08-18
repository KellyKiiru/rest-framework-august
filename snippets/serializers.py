from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

"""
serializer.ModelSerializer makes it easier to serialize your models. You write less code with it
"""
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Snippet
        # fields = ['__all__']
        fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id','username','snippets']