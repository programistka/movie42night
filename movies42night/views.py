from django.http import HttpResponse
from django.shortcuts import render

from movies42night.models import Movie


def index(request):
    return HttpResponse("Hello, world. This is index.")


def detail(request, movie_id):
    movie_details = Movie.objects.get(id=movie_id)
    context = {
        'movie_details': movie_details
    }
    return render(request, 'movies42night/detail.html', context)


def list(request):
    movies = Movie.objects.all()
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


def add(request):
    if request.method == 'POST':
        movie = Movie(title=request.POST['title'])
        movie.save()
    context = {
        'tt': 'tt'
    }
    return render(request, 'movies42night/add.html', context)
