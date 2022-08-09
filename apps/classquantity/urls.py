from django.urls import path
from .views import ClassQuantityListAPIView, ClassQuantityCreateAPIView, ClassQuantityDetailAPIView, ClassQuantityUpdateAPIView, ClassQuantityDeleteAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ClassQuantityListAPIView.as_view(), name='list'),
    path('create/', ClassQuantityCreateAPIView.as_view(), name='create'),
    path('<int:id>/', ClassQuantityDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', ClassQuantityUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', ClassQuantityDeleteAPIView.as_view(), name='delete'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
