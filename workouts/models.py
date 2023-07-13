from django.db import models
from django.contrib.auth.models import User


# Create your models here:
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # weight in kilograms
    workout = models.ForeignKey('Workout', related_name='exercises', on_delete=models.CASCADE)


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    workouts = models.ManyToManyField(Workout)
