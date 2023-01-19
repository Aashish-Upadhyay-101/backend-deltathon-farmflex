from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from farm.settings import AUTH_USER_MODEL
from apps.common.models import TimeStampUUIDModel

User = get_user_model()


class ProfileType(models.TextChoices):
    FARMER = "Farmer", "Famer"
    COLD_STORE = "Cold_Store", "Cold store"
    CONSUMER = "Consumer", "Consumer user"


class Profile(TimeStampUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(default="Nepal", max_length=128, blank=False, null=False)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    profile_type = models.CharField(max_length=30, choices=ProfileType.choices, default=ProfileType.FARMER, blank=False, null=False)


    def __str__(self):
        return self.user.username



@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()