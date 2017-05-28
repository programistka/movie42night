from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
