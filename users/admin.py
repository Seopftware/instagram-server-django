from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile Info", {
                "fields": ("email", "password", "nickname", "profileImg", "profileIntroduce", "followerNumber"),
                "classes": ("wide",),
            },
        ),
    )

    list_display = ("email", "nickname", "followerNumber")
