from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile (models.Model):

    SUBJECT_CHOICES = [
        ('EN', 'English'),
        ('MA', 'Math'),
        ('PH', 'Phyiscs'),
        ('CH', 'Chemist'),
        ('BI', 'Biology')
    ]

    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='profile')
    teachers_field = models.CharField (max_length=2, choices=SUBJECT_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username