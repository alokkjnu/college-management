from django.urls import path
from rest_framework.routers import DefaultRouter

from ..api.views import BlogView
router = DefaultRouter()
router.register('blog', BlogView, basename='blog')
urlpatterns = [
    # path('', include(router.urls)),
    path('', BlogView.as_view(), name='blog'),
    path('<int:id>', BlogView.as_view(), name='blog'),
]