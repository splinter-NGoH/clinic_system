from django.urls import path

from software_medical.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    profile_view,
    admin_dashboard_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("profile/<str:username>/", profile_view, name="profile"),
]
