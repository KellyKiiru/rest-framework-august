from rest_framework import status
from rest_framework import mixins
from rest_framework import generics 
"""
One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behaviour.
"""


from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)