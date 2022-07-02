from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer

class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer
    
class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer
    
class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer
    