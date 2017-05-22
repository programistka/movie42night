from django.contrib import admin

from .models import Movie, Type

admin.site.register(Movie)
admin.site.register(Type)