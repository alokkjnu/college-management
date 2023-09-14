from django.urls import path
from rest_framework.routers import DefaultRouter

from ..api.views import CourseView, SubjectView

router = DefaultRouter()
router.register('course', CourseView, basename='course')
urlpatterns = [
    # path('', include(router.urls)),
    path('', CourseView.as_view(), name='course'),
    path('<int:id>', CourseView.as_view(), name='course'),
    path('subject', SubjectView.as_view(), name='subject'),
    path('subject/<int:id>', SubjectView.as_view(), name='subject'),
]
