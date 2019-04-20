from django.db import models

from accounts.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, unique=True, primary_key=True, auto_created=False)
    short_description = models.TextField(blank=False)
    description = models.TextField(blank=False)
    outcome = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    price = models.FloatField()
    level = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video_url = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
