from django.shortcuts import render, redirect, get_object_or_404

from filmweb import Filmweb

from movies42night.forms import MovieForm, MovieProcessForm
from movies42night.models import Movie, Status, Details, User


#@login_required
def index(request):
    #reported by user and rejected by others
    rejected = Movie.objects.filter(user_id=1).filter(status_id=3)
    #no matter who reported - everyone accepted
    accepted = Movie.objects.filter(status_id=2)
    context = {
        'rejected': rejected,
        'accepted': accepted,
    }
    return render(request, 'movies42night/dashboard.html', context);


#@login_required
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    details = Details.objects.get(movie=movie)
    context = {
        'movie': movie,
        'details': details
    }
    return render(request, 'movies42night/detail.html', context)


#@login_required
def list_all(request):
    print("list all")
    movies = Movie.objects.all()
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


#@login_required
def list_accepted(request):
    movies = Movie.objects.filter(status=2)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


#@login_required
def list_rejected(request):
    movies = Movie.objects.filter(status=3)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


#@login_required
def list_new(request):
    movies = Movie.objects.filter(status=1)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


#@login_required
def list_private(request):
    movies = Movie.objects.filter(status=3).filter(status=4)
    context = {
        'movies_list': movies
    }
    return render(request, 'movies42night/list.html', context)


#@login_required
def add(request):
    if request.method == "POST":
        user = User.objects.get(email=request.user.email)
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            fw = Filmweb()
            movies = fw.search_movie(post.title)
            movie = Movie.objects.get(id=post.id)
            Details.objects.create(movie = movie, description_from_filmweb=movies[0]['desc'], rating_from_filmweb=movies[0]['votinginfo'])
            context = {
                'movie_desc': movies[0]['desc']
            }
            return render(request, 'movies42night/getfilmwebinformation.html', context)
    else:
        form = MovieForm()
    return render(request, 'movies42night/add.html', {'form': form})


#@login_required
def get_filmweb_information(request, title):
    fw = Filmweb()
    movies = fw.search_movie(title)
    context = {
        'movie_desc': movies[0]['desc']
    }
    return render(request, 'movies42night/getfilmwebinformation.html', context)


#@login_required
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
            if 'delete' in request.POST:
                movie.delete()
                return redirect('/movies42night/movies/all')