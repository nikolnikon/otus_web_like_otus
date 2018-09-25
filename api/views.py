from rest_framework import mixins, viewsets
from django.contrib.auth import get_user_model

from courses.models import Course
from api.serializers import UserSerializer, CourseSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
