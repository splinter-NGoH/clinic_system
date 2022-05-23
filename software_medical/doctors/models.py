from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

User = get_user_model()


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    doctor_name = models.CharField(max_length=254)
    specializations = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("doctor")
        verbose_name_plural = _("doctors")

    def __str__(self):
        return "D/" + self.doctor_name + "  specialization:  " + self.specializations
