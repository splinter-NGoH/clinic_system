from django.conf import settings
from software_medical.appointment.models import Appoinment


def allauth_settings(request):
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }


def get_appoinments(request):
    all_appoinments = Appoinment.objects.all()
    return {"ALL_APPOINMENT": all_appoinments}
