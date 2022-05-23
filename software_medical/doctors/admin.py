from django.contrib import admin
from .models import Doctor


class AdminDoctor(admin.ModelAdmin):
    list_display = [
        "user",
        "doctor_name",
        "specializations",
        "created_at",
    ]
    search_fields = [
        "doctor_name",
        "specializations",
        "created_at",
    ]
    filter_fields = [
        "doctor_name",
        "specializations",
        "created_at",
    ]

    ordering = ("-created_at",)


admin.site.register(Doctor, AdminDoctor)
