from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import RegexValidator

class User(AbstractUser):
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    def __str__(self):
        return "{}".format(self.email)
class UserProfile(models.Model):
    # Create relationship
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
   
    # Additional fields
    STATUS_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    sex = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Prefer not to say")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+254'. Up to 15 digits allowed.")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True, default=None)
