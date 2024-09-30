from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserDetails(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MEDI_CONDITION = (
        ('Diabetes', 'Diabetes'),
        ('Pre-Diabetes', 'Pre-Diabetes'),
        ('Cholesterol', 'Cholesterol'),
        ('Hypertension', 'Hypertension'),
        ('Thyroid', 'Thyroid'),
    )
    EMOTIONAL_HEALTH_OPT = (
        ('Excessive Stress', 'Excessive Stress'),
        ('Sleep Issues', 'Sleep Issues'),
        ('Anger Issues', 'Anger Issues'),
        ('Loneliness', 'Loneliness'),
        ('Relationship stress', 'Relationship stress'),
        )
    user_acc = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    mob_no = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    user_height = models.CharField(max_length=200, blank=True, null=True)
    user_weight = models.CharField(max_length=200, blank=True, null=True)
    target_weight = models.CharField(max_length=200, blank=True, null=True)
    medical_condition = models.CharField(
        max_length=200, choices=MEDI_CONDITION, blank=True, null=True)
    emotional_health = models.CharField(
        max_length=200, choices=EMOTIONAL_HEALTH_OPT, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)


class Trainer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mob_no = models.CharField(max_length=255, blank=True, null=True)
    expertise = models.CharField(max_length=255, blank=True, null=True)
    experince = models.IntegerField(blank=True, null=True)

class UserQuery(models.Model):
    user_acc = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=100)
    user_query_message = models.TextField()
    send_time = models.DateTimeField(default=timezone.now) 

class ExerciesCategory(models.Model):
    BODYPART_LIST = (
        ('Arms', 'Arms'),
        ('Back', 'Back'),
        ('Chest', 'Chest'),
        ('Legs', 'Legs'),
        ('Feet', 'Feet'),
        ('Forearms', 'Forearms'),
        ('Glutes', 'Glutes'),
        ('Head', 'Head'),
        ('Inseam', 'Inseam'),
        ('Jaw', 'Jaw'),
        ('Knee', 'Knee'),
        ('Legs', 'Legs'),
        ('Muscle', 'Muscle'),
        ('Neck', 'Neck'),
        ('Other', 'Other'),
    )
    EXCERCIES_NAME = (
        ('squat','squat'),
        ('deadlift','deadlift'),
        ('legpress','legpress'),
        ('dumbellfly','dumbellfly'),
        ('chestpress','chestpress'),
        ('overheadpress','overheadpress'),
        ('legcurl','legcurl'),
        ('abtwister','abtwister'),
        ('plank','plank'),
        ('biceps','biceps'),
        ('triceps','triceps'),
        ('crunches','crunches'),
        ('pushup','pushup'),
        ('pullups','pullups')
    )
    body_part = models.CharField(max_length=10, choices=BODYPART_LIST)
    e_name = models.CharField(max_length=15, choices=EXCERCIES_NAME)


class Excercies(models.Model):
    e_name = models.ForeignKey(User, on_delete=models.CASCADE)
    e_type = models.ForeignKey(ExerciesCategory, on_delete=models.CASCADE)
    favorites = models.BooleanField(default=False)

    
class Schedule(models.Model):
    DAYS_LIST = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10,choices=DAYS_LIST)
    activity = models.ForeignKey(Excercies,on_delete=models.CASCADE ,null=True, blank=True)


class Feedback(models.Model):
    uname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    satisfy = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    msg = models.TextField()

