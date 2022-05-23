from django.contrib import admin
from .models import Appoinment


class AdminAppoinment(admin.ModelAdmin):
    list_display = [
        "user",
        "doctor",
        "full_name",
        "email",
        "date",
        "time",
        "Syndrome",
        "is_done",
        "created_at",
    ]
    search_fields = [
        "full_name",
        "email",
        "date",
        "time",
        "Syndrome",
        "created_at",
    ]
    filter_fields = [
        "full_name",
        "email",
        "date",
        "time",
        "Syndrome",
        "is_done",
        "created_at",
    ]

    ordering = ("-created_at",)
    list_editable = ("is_done",)


admin.site.register(Appoinment, AdminAppoinment)
