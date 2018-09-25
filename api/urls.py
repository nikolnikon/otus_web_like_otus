from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, CourseViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
