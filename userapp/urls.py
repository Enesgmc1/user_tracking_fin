from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, TodoViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)
router.register('todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
