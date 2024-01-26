from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def send_activate_email(sender, instance, created, **kwargs):
    if created:
        send_mail("Test subject", "Test message", "zasurzuraev25gmail.com", [instance.email])
