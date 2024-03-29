from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'is_staff', 'is_active', 'date_joined', 'role')
    list_filter = ('email', 'first_name', 'is_staff', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2',
                       'is_staff', 'is_active', 'role')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
