from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Topic(models.Model):
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
    topic_name    = models.CharField(max_length=200)
    start_date    = models.DateField()
    end_date      = models.DateField()
    duration_days = models.IntegerField(editable=True)
    created_at    = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at   = models.DateTimeField(null=True, auto_now=True, editable=False)

    def __str__(self):
        return self.topic_name

class Task(models.Model):
    SYSTEM_DEFINED_UNITS = [
        ('nos', 'nos'),
        ('hrs', 'hours'),
        ('kms', 'Kilometres')
    ]

    taskname            = models.CharField(max_length=200)
    topic_id            = models.ForeignKey(Topic, on_delete=models.CASCADE, db_column="topic_id")
    user_id             = models.ForeignKey(User,  on_delete=models.CASCADE)
    times               = models.FloatField()
    system_defined_unit = models.CharField(max_length=10, choices=SYSTEM_DEFINED_UNITS, null=True, blank=True)
    user_defined_unit   = models.CharField(max_length=10, null=True, blank=True)
    completed_times     = models.FloatField(null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at         = models.DateTimeField(null=True, auto_now=True, editable=False)

    def __str__(self):
        return self.taskname
    
class UserDefinedUnits(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    unit    = models.CharField(max_length=10)

class TaskCompletion(models.Model):
    user_id   = models.ForeignKey(User,  on_delete=models.CASCADE)
    topic_id  = models.ForeignKey(Topic, on_delete=models.CASCADE)
    task_id   = models.ForeignKey(Task,  on_delete=models.CASCADE)
    timestamp = models.DateTimeField()


def all_records(model_name):
    return model_name.objects.all().order_by('id')