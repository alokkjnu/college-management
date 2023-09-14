from django.urls import path

from ..api.views import CollegeView

urlpatterns = [
    path('', CollegeView.as_view(), name='college'),
    path('<int:id>', CollegeView.as_view(), name='college'),
]