from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime


# Create your models here.

class UserManager(BaseUserManager):
    # create and return user with email, username and password
    def create_user(self, email, password):
        if email is None:
            raise TypeError("User must have an email")
        if password is None:
            raise TypeError("User must have a password")
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    # create and return user with superuser (admin) permission
    def create_superuser(self, email, password):
        if password is None:
            raise TypeError("Superuser must have a password")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        if password is not None:
            user.set_password(password)
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    # gender = models.CharField(choices = GenderChoices.choices, max_length = 100, null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = False)
    # country = models.ForeignKey(Country, on_delete = models.SET_NULL, blank = True, null = True)
    # state = models.ForeignKey(State, on_delete = models.SET_NULL, blank = True, null = True)
    city = models.CharField(max_length = 100, null = True, blank = False)
    zip_code = models.CharField(max_length=10,blank=True, null=True)
    mobile_number = models.CharField(max_length = 100, null = True, blank = False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = "email"
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

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