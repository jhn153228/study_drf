from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView
)

urlpatterns = [
    # path('api-token-auth/', obtain_auth_token),
    path('api-jwt-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-jwt-auth/refresh/', TokenVerifyView.as_view(), name='token_refresh'),
    path('api-jwt-auth/verify/', TokenRefreshView.as_view(), name='token_refresh'),
]