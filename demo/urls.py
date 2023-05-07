from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet, AlbumViewSet, TrackViewSet

# viewset
router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('albums', AlbumViewSet)
router.register('track', TrackViewSet)

urlpatterns = [
    # we can check out the registered url
    path('', include(router.urls)),
    path('first/', views.first),
    path('another', views.Another.as_view()),
    # generic view
    path('another/book/', views.BookList.as_view())
]