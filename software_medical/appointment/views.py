from django.shortcuts import render
from .forms import AppointmentForms
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
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
            return redirect("appointment")

    else:
        form = AppointmentForms(request.user)
    return render(
        request,
        "pages/home_view.html",
        {
            "form": form,
        },
    )


def appointment_view(request):
    form = AppointmentForms(request.user)
    if request.method == "POST":
        form = AppointmentForms(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Apointment submitted successfully")
            return HttpResponseRedirect(
                "/users/profile/{}/".format(request.user.username)
            )

    return render(request, "pages/appointment.html", {"form": form})


def about_view(request):
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
            return redirect("appointment")

    else:
        form = AppointmentForms(request.user)
    return render(
        request,
        "pages/about.html",
        {
            "form": form,
        },
    )
