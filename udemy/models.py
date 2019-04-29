from django.db import models
from django.utils.timezone import now

from accounts.models import User
from courses.models import Course


class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolls')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
