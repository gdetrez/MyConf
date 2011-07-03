from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User)

    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="avatars", blank=True)
    #team involvement??
    blogs = models.URLField(blank=True, verify_exists=False)
    microblogs = models.URLField(blank=True, verify_exists=False)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    micro_biography = models.CharField(max_length=140, blank=True)
    physical_location = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
