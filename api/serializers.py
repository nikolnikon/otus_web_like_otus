from rest_framework import serializers
from django.contrib.auth import get_user_model

from courses.models import Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'about', 'is_student', 'is_tutor')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ()
