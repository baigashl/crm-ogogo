from django.urls import path
from .views import (
    ClassQuantityListAPIView, ClassQuantityCreateAPIView,
    ClassQuantityDetailAPIView, ClassQuantityUpdateAPIView,
    ClassQuantityDeleteAPIView,
    StudentClassQuantityListAPIView, StudentClassQuantityCreateAPIView,
    StudentClassQuantityDetailAPIView, StudentClassQuantityUpdateAPIView,
    StudentClassQuantityDeleteAPIView
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ClassQuantityListAPIView.as_view(), name='list'),
    path('create/', ClassQuantityCreateAPIView.as_view(), name='create'),
    path('<int:id>/', ClassQuantityDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', ClassQuantityUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', ClassQuantityDeleteAPIView.as_view(), name='delete'),

    # student class quantity
    path('student/', StudentClassQuantityListAPIView.as_view(), name='student-list'),
    path('student/create/', StudentClassQuantityCreateAPIView.as_view(), name='student-create'),
    path('student/<int:stud_id>/', StudentClassQuantityDetailAPIView.as_view(), name='student-detail'),
    path('student/<int:stud_id>/<int:course_id>/update', StudentClassQuantityUpdateAPIView.as_view(), name='student-update'),
    path('student/<int:id>/delete/', StudentClassQuantityDeleteAPIView.as_view(), name='student-delete'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
