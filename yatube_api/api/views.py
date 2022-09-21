from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, filters, mixins
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer
)
from posts.models import Post, Comment, Group, Follow

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class GroupVeiwSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReadOrCreateFollowForUser(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    pass


class FollowViewSet(ReadOrCreateFollowForUser):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
