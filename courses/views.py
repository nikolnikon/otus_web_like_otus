from django.views.generic import ListView, DetailView

from courses.models import Course


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course

