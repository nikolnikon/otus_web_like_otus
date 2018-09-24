from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views


app_name = 'api'

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
