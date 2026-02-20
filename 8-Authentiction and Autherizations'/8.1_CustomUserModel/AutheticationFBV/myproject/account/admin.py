from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserModelAdmin(UserAdmin):
    model = User
    ordering = ("email",)   # 🔥 FIX HERE

    list_display = (
        "id",
        "email",
        "name",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_customer",
        "is_seller",
        "created_at",
    )

    list_filter = ("is_superuser",)

    search_fields = ("email", "name", "city")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name", "city")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "is_customer",
                    "is_seller",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "city",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_customer",
                    "is_seller",
                ),
            },
        ),
    )

    readonly_fields = ("created_at", "updated_at", "last_login")


admin.site.register(User, UserModelAdmin)
