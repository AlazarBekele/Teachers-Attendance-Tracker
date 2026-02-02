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
    

class PeriodContainer (models.Model):

    CLASSROOMS = [
        ('A', 'a'),('B', 'b'),('C', 'c'),('D', 'd'),('F', 'e'),
        ('G', 'g'),('H', 'h')
    ]

    DAYS = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    ]

    PERIODS = [
        (1, '1st Period'),
        (2, '2nd Period'),
        (3, '3rd Period'),
        (4, '4th Period'),
        (5, '5th Period'),
        (6, '6th Period'),
    ]

    teachers = models.ForeignKey (Profile, on_delete=models.CASCADE)
    day = models.CharField (max_length=3, choices=DAYS)
    period = models.IntegerField (choices=PERIODS)
    classroom = models.CharField (max_length=1, choices=CLASSROOMS, null=True, blank=True)

    class Meta:
        unique_together = ('teachers', 'day', 'period', 'classroom')

    def __str__(self):
        return self.teachers.user.first_name