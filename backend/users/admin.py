from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "avatar_preview",
        "username",
        "email",
        "phone",
        "role",
        "is_active",
        "email_verified",
        "date_joined",
    )

    list_filter = (
        "role",
        "gender",
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "phone_verified",
        "date_joined",
    )

    search_fields = (
        "username",
        "email",
        "phone",
        "first_name",
        "last_name",
    )

    ordering = ("-date_joined",)

    readonly_fields = (
        "avatar_preview",
        "last_login",
        "date_joined",
    )

    fieldsets = (
        ("Authentication", {
            "fields": ("username", "password"),
        }),
        ("Personal information", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "phone",
                "avatar",
                "avatar_preview",
                "birth_date",
                "gender",
                "city",
                "bio",
            ),
        }),
        ("Verification", {
            "fields": (
                "email_verified",
                "phone_verified",
            ),
        }),
        ("Permissions", {
            "fields": (
                "role",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        ("Important dates", {
            "fields": (
                "last_login",
                "date_joined",
            ),
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "role",
                ),
            },
        ),
    )

    @admin.display(description="Avatar")
    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%;">',
                obj.avatar.url,
            )
        return "—"