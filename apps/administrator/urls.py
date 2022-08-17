
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (
    MyObtainPairView,
    CreateSubAdminView,
    SubAdminListAPIView
)

urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create_subadmin/', CreateSubAdminView.as_view(), name='register'),
    path('list_subadmin/', SubAdminListAPIView.as_view(), name='list'),
]

