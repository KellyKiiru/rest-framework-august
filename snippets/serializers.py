from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedRelatedField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        # fields = ['__all__']
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','id','username','snippets']