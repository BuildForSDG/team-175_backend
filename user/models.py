from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
"""
The user model 

"""


class User(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField( max_length=254)
    STATUS_CHOICES = (
                    ('Female', 'Female'),
                    ('Male', 'Male'),
                    ('Prefer not to say', 'Prefer not to say'),
                    )
    Sex = models.CharField(max_length=50, choices = STATUS_CHOICES, default = "Prefer not to say")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    PhoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    
    class Meta:
        ordering = ('FirstName',)
    
    
    
    def __str__(self):
        return self.FirstName
   