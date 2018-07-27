from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

# todo Разобраться, как отображать дополнительные поля при передаче в register BaseUserModel

admin.site.register(User)
