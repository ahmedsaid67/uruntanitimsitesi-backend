from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Contact,Hakkimizda

@receiver(post_migrate)
def create_initial_contact(sender, **kwargs):
    if sender.name == 'myapp':
        if not Contact.objects.exists():
            Contact.objects.create()


@receiver(post_migrate)
def create_initial_hakkimizda(sender, **kwargs):
    if sender.name == 'myapp':
        if not Hakkimizda.objects.exists():
            Hakkimizda.objects.create()
