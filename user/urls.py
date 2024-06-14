from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('delete/', UserDeleteAPIView.as_view()),
    path('details/', UserDetailsAPIView.as_view()),
    path('update/', UserUpdateAPIView.as_view()),
]
