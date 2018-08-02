from django.contrib.auth import get_user_model

from registration.forms import RegistrationForm

from users.models import User


class CustomRegistrationForm(RegistrationForm):
    class Meta:
        model = User
        fields = (getattr(get_user_model(), 'USERNAME_FIELD', 'username'), 'email', 'first_name', 'last_name')
