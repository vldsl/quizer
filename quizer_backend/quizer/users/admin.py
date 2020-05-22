from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser')
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_teacher']
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
