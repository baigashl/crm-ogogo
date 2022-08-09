from django.urls import path
from .views import CourseListAPIView, CourseCreateAPIView, CourseDetailAPIView, CourseUpdateAPIView, CourseDeleteAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='list'),
    path('create/', CourseCreateAPIView.as_view(), name='create'),
    path('<int:id>/', CourseDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', CourseUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', CourseDeleteAPIView.as_view(), name='delete'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
