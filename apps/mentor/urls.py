from django.urls import path
from .views import MentorListAPIView, MentorCreateAPIView, MentorDetailAPIView, MentorUpdateAPIView, MentorDeleteAPIView

urlpatterns = [
    path('', MentorListAPIView.as_view(), name='list'),
    path('create/', MentorCreateAPIView.as_view(), name='create'),
    path('<int:id>/', MentorDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update', MentorUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', MentorDeleteAPIView.as_view(), name='delete'),
]



