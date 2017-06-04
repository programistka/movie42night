from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from filmweb import Filmweb

from movies42night.forms import MovieForm, MovieProcessForm
from movies42night.models import Movie, Status



def index(request):
    return HttpResponse("Hello, world. This is index.")


def detail(request, movie_id):
    movie_details = Movie.objects.get(id=movie_id)
    context = {
        'movie_details': movie_details
    }
    return render(request, 'movies42night/detail.html', context)


def list_all(request):
    print("list all")
    movies = Movie.objects.all()
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


def list_accepted(request):
    movies = Movie.objects.filter(status=2)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


def list_rejected(request):
    movies = Movie.objects.filter(status=3)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


def list_new(request):
    movies = Movie.objects.filter(status=1)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


def list_private(request):
    movies = Movie.objects.filter(status=3).filter(status=4)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


def add(request):
    if request.method == "POST":
        fw = Filmweb()
        movies = fw.search_movie("Kruk")
        print(movies[0]['desc'])
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/movies42night/movies/all', pk=post.pk)
    else:
        form = MovieForm()
    return render(request, 'movies42night/add.html', {'form': form})


def process_movie(request, pk):
    print("process movie")
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        print("post")
        form = MovieProcessForm(request.POST, instance=movie)
        print("form is valid", form.is_valid(), form.errors)
        if form.is_valid():
            if 'accepted' in request.POST:
                movie.status = Status.objects.get(id=2)
                movie.save()
                return redirect('/movies42night/movies/accepted')
            if 'rejected' in request.POST:
                movie.status = Status.objects.get(id=3)
                movie.save()
                return redirect('/movies42night/movies/rejected')
