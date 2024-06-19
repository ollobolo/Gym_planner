from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    BODY_PART_CHOICES = [
        ('klata', 'Klata'),
        ('plecy', 'Plecy'),
        ('biceps', 'Biceps'),
        ('triceps', 'Triceps'),
        ('barki', 'Barki'),
        ('nogi', 'Nogi'),
        ('cardio', 'Cardio'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    part = models.CharField(max_length=10, choices=BODY_PART_CHOICES, default='data')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    date_added = models.DateTimeField(auto_now_add=True)

