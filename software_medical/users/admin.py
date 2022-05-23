from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from software_medical.users.forms import UserAdminChangeForm, UserAdminCreationForm
from software_medical.users.models import Profile

User = get_user_model()

admin.site.site_header = "clinic system"
admin.site.site_title = "clinic"
admin.site.index_title = " Admin"


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password", "email")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
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
                "fields": ("username", "email", "groups", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


class AdminProfile(admin.ModelAdmin):
    list_display = (
        "bio",
        "location",
        "birth_date",
        "created_at",
    )
    search_fields = (
        "bio",
        "location",
        "birth_date",
    )
    filter_fields = [
        "bio",
        "location",
        "birth_date",
    ]


admin.site.register(Profile, AdminProfile)
