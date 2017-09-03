from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Details(models.Model):
    description_from_filmweb = models.TextField(max_length=10000, null=True)
    rating_from_filmweb = models.CharField(max_length=100, null=True)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)



