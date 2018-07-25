from django.urls import path

from courses.views import CourseListView, CourseDetailView


urlpatterns = [
    path('', CourseListView.as_view(), name='detail'),
    path('<int:pk>/', CourseDetailView.as_view(), name='detail'),
]