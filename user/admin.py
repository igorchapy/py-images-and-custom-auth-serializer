from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    ordering = ['email']  # or any valid field from your User model
    list_display = ['email', 'is_staff']  # customize as needed

    # If you use AbstractBaseUser, define form and add_fieldsets

admin.site.register(User, CustomUserAdmin)
