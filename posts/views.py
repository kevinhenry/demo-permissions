from rest_framework import generics, permissions, serializers
from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

