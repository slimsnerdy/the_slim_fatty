from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


# Create your models here.

class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(null=True, blank=True)
    pass

    def __str__(self):
        return self.username

# https://learndjango.com/tutorials/django-custom-user-model


class CustomSite(Site):
    meta_description = models.CharField(max_length=200, blank=False)
    # pass

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"