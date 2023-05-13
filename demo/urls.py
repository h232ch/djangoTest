from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet, AlbumViewSet, TrackViewSet, ClassBasedViewBooks

# viewset
router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('albums', AlbumViewSet)
router.register('track', TrackViewSet)

urlpatterns = [
    # we can check out the registered url
    path('', include(router.urls)),

    # class based view example
    path('cviewbooks/', views.ClassBasedViewBooks.as_view()),
    path('cviewbooks/<int:pk>/', views.ClassBasedViewBookDetail.as_view()),

    # class based view with mixin
    path('mixinviewbooks/', views.MixingViewBooks.as_view()),
    path('mixinviewbooks/<int:pk>/', views.MixingViewDetailBook.as_view()),

    # function based view
    path('functionviewbooks/', views.function_based_view_books),
    path('functionviewbooks/<int:pk>/', views.function_based_view_detail_book),


    path('first/', views.first),
    path('another', views.Another.as_view()),
    # generic view
    path('another/book/', views.BookList.as_view())
]