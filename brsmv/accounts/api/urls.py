from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..api.views import registration_view, logout_view
router = DefaultRouter()
router.register('register', registration_view, basename='register')
# router.register('logout', logout_view, basename='logout')
# router.register('login', obtain_auth_token, basename='login')

urlpatterns = [
    # path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout')
]
