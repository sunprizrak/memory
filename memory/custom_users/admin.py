from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, CustomGroup

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(CustomGroup)
class CustomGroupAdmin(GroupAdmin):
    pass