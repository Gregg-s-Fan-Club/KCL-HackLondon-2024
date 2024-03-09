from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
import greggor_productivity_companion.models as fcmodels

class User(AbstractUser):
    """User model used for authentication"""

    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{1,}$',
            message='Username must consist of @ followed by at least one letter or number'
        )]
    )
    email = models.EmailField(unique=True, blank=False)
    points = models.IntegerField(blank=False, default = 0)

    def get_user_points(self, category_type = "ALL"):
        if category_type == "ALL":
            tasks = Task.objects.filter(user = self)
        else:
            tasks = Task.objects.filter(user = self, category = category_type)
        points = 0
        for task in tasks:
            points += task.get_task_points()
        return points
            
    