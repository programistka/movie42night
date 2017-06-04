from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)
    description_from_filmweb = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
