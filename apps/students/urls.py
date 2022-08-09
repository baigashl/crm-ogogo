from django.urls import path
from .views import StudentListAPIView, StudentCreateAPIView, StudentDetailAPIView, StudentUpdateAPIView, StudentDeleteAPIView

urlpatterns = [
    path('', StudentListAPIView.as_view(), name='list'),
    path('create/', StudentCreateAPIView.as_view(), name='create'),
    path('<int:id>/', StudentDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', StudentUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', StudentDeleteAPIView.as_view(), name='delete'),
]
