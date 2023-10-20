from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateAPIView, Logout, UserListAPIView, UserDetailAPIView, UserDeleteAPIView, \
    UserProfileAPIView, CustomAuthToken, Home

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='token_obtain_pair'),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListAPIView.as_view()),
    path('profile/', UserProfileAPIView.as_view()),
    path('<int:pk>/', UserDetailAPIView.as_view()),
    path('<int:pk>/delete/', UserDeleteAPIView.as_view()),
]
