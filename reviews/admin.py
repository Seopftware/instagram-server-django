from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
        list_display = (
        "content",
        "like",
        "owner",
        "created_at",
        "updated_at"
    )
