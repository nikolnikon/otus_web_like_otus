from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from users.models import User


# todo Разобраться, как отображать дополнительные поля при передаче в register BaseUserModel
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    fieldsets = [BaseUserAdmin.fieldsets].append(('Additional fields', {'fields': ('is_student', 'is_tutor')}))


admin.site.register(User, CustomUserAdmin)
