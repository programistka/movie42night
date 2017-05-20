from django.http import HttpResponse
from django.template import loader

from movies42night.models import Movie


def index(request):
    return HttpResponse("Hello, world. This is index.")

def detail(request, movie_id):
    movie_details = Movie.objects.get(id=movie_id)
    template = loader.get_template('movies42night/detail.html')
    context = {
        'movie_details': movie_details,
    }
    return HttpResponse(template.render(context, request))

