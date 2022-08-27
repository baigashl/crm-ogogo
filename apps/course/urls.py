from django.urls import path
from .views import (
    CourseListAPIView,
    CourseCreateAPIView,
    CourseDetailAPIView,
    CourseUpdateAPIView,
    CourseDeleteAPIView,
    ArchiveCourseListAPIView,
    CourseMoveToArchiveAPIView
)

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='list'),
    path('create/', CourseCreateAPIView.as_view(), name='create'),
    path('<int:id>/', CourseDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', CourseUpdateAPIView.as_view(), name='update'),
    path('<int:id>/move_to_archive/', CourseMoveToArchiveAPIView.as_view(), name='move_to_archive'),
    path('<int:id>/delete/', CourseDeleteAPIView.as_view(), name='delete'),
    path('archive/', ArchiveCourseListAPIView.as_view(), name='archive'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
