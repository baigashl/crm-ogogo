from django.urls import path
from .views import AdministratorListAPIView, AdministratorCreateAPIView, AdministratorDeleteAPIView, AdministratorDetailAPIView, AdministratorUpdateAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', AdministratorListAPIView.as_view(), name='list'),
    path('create/', AdministratorCreateAPIView.as_view(), name='create'),
    path('<int:id>/', AdministratorDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', AdministratorUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', AdministratorDeleteAPIView.as_view(), name='delete'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
