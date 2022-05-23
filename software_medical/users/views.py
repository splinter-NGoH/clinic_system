from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from software_medical.appointment.models import Appoinment
from software_medical.appointment.forms import AppointmentForms
from django.contrib import messages
from django.http import HttpResponseRedirect

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["username"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        # return self.request.user.get_absolute_url()
        return reverse("users:profile", kwargs={"username": self.request.user.username})

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:profile", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


def profile_view(request, username):
    if request.method == "POST":
        form = AppointmentForms(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your appoinment submitted successfully")
            return HttpResponseRedirect(
                "/users/profile/{}/".format(request.user.username)
            )
        else:
            messages.error(request, "wrong inputs")
            return redirect("appoinment_home")

    else:
        form = AppointmentForms(request.user)
    appointments = Appoinment.objects.filter(user__username=username, is_done=False)
    context = {
        "appointments": appointments,
        "form": form,
    }
    return render(request, "pages/profile.html", context)


def admin_dashboard_view(request):
    return render(request, "pages/admin_dashboard.html")
