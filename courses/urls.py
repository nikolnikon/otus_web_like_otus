from django.urls import path

from courses.views import CourseListView, CourseDetailView


app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='detail'),
]
