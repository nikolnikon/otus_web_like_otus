from django.urls import path, include
from django.views.generic import TemplateView

from registration.backends.simple.views import RegistrationView

from users.forms import CustomRegistrationForm

app_name = 'users'

urlpatterns = [
    path('register/',
         RegistrationView.as_view(form_class=CustomRegistrationForm),
         name='registration_register'),
    path('register/complete/',
         TemplateView.as_view(template_name='registration/registration_complete.html'),
         name='registration_complete'),
]
