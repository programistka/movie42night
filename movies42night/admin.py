from django.contrib import admin

from .models import Movie, Status

admin.site.register(Movie)
admin.site.register(Status)