from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from registration.backends.simple.views import RegistrationView
from users.forms import CustomRegistrationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=CustomRegistrationForm),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
