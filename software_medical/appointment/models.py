from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from software_medical.doctors.models import Doctor
from django.core.exceptions import ValidationError
import datetime
from django.contrib import messages
from django.shortcuts import redirect

User = get_user_model()


class Appoinment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    Syndrome = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Appoinment")
        verbose_name_plural = _("Appoinments")
        unique_together = ("date", "time")

    def __str__(self):
        return self.full_name
