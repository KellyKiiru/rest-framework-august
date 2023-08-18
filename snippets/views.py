from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import generics 
from .permissions import IsOwnerOrReadOnly

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

"""
Using the mixin classes we've rewritten the views to use slightly less code than before, but we can go one step further. REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more.
"""

class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer