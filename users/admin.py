from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile Info", {
                "fields": ("email", "password", "nickname"),
                "classes": ("wide",),
            },
        ),
    )