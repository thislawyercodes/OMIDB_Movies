from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api.views.auth_views import CreateUserApiView,ListUsersAPIView, ObtainTokenPairAPIView, PasswordResetApiView, SetInitialPasswordApiView, UserApiView

urlpatterns = [
    path('token', ObtainTokenPairAPIView.as_view(), name='token'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('set-password/<str:id>', SetInitialPasswordApiView.as_view(), name='password_reset'),
    path('reset-password', PasswordResetApiView.as_view(), name='password_reset'),
    path('list', ListUsersAPIView.as_view(), name='list_users'),
    path('user', CreateUserApiView.as_view(), name='user_create'),
    path('user/<uuid:id>', UserApiView.as_view(), name="user"),
]
