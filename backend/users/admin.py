from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

def badge(text, color):
    return format_html(
        '<span style="background:{};color:white;padding:5px 10px;border-radius:20px;font-weight:600;font-size:12px;">{}</span>',
        color,
        text,
    )

from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    @admin.action(description="Deactivate selected users")
    def deactivate_users(self, request, queryset):
        updated = queryset.update(is_active=False)

        self.message_user(
            request,
            f"{updated} users were deactivated.",
            level=messages.SUCCESS,
        )

    @admin.action(description="Activate selected users")
    def activate_users(self, request, queryset):
        updated = queryset.update(is_active=True)

        self.message_user(
            request,
            f"{updated} users were activated.",
            level=messages.SUCCESS,
        )

    @admin.action(description="Verify Email")
    def verify_email(self, request, queryset):
        updated = queryset.update(email_verified=True)

        self.message_user(
            request,
            f"Verified email for {updated} users.",
            level=messages.SUCCESS,
        )

    @admin.action(description="Unverify Email")
    def unverify_email(self, request, queryset):
        updated = queryset.update(email_verified=False)

        self.message_user(
            request,
            f"Unverified email for {updated} users.",
            level=messages.SUCCESS,
        )

    @admin.display(description="Role", ordering="role")
    def role_badge(self, obj):
        colors = {
        User.Role.USER: "#2563eb",        # blue
        User.Role.MODERATOR: "#d97706",  # orange
        User.Role.ADMIN: "#dc2626",      # red
        }

        return badge(obj.get_role_display(), colors.get(obj.role, "#6b7280"))

    @admin.display(description="Status", ordering="is_active")
    def status_badge(self, obj):
        if obj.is_active:
            return badge("Active", "#16a34a")

        return badge("Inactive", "#dc2626")

    @admin.display(description="Email")
    def email_status(self, obj):
        if obj.email_verified:
            return badge("Verified", "#16a34a")

        return badge("Unverified", "#dc2626")

    @admin.display(description="Phone")
    def phone_status(self, obj):
        if obj.phone_verified:
            return badge("Verified", "#16a34a")

        return badge("Unverified", "#dc2626")

    list_display = (
        "id",
        "avatar_preview",
        "username",
        "email",
        "phone",
        "role_badge",
        "status_badge",
        "email_status",
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

    actions = (
        "activate_users",
        "deactivate_users",
        "verify_email",
        "unverify_email",
    )
    