from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, GroupVeiwSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register(r'groups', GroupVeiwSet)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
