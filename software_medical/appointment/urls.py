from django.urls import path
from .views import home_view, appointment_view, about_view

urlpatterns = [
    path("", home_view, name="home_view_template"),
    path("about/", about_view, name="about"),
    path("appointment/", appointment_view, name="appointment"),
]
