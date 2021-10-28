from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from movies.models import Movie

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {
        "title": "Movies List",
        "movies" : movies
    }
    return render(request, "movies.html", context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        "title" : "Movie",
        "movie" : movie
    }
    return render(request, "detail.html", context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        date_released = request.POST["date_released"]
        Movie.objects.create(title=title, date_released=date_released)
        return HttpResponseRedirect(reverse("movies_list"))
    else:
        return render(request, "create.html")

def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        title = request.POST["title"]
        date_released = request.POST["date_released"]

        movie.title = title
        movie.date_released = date_released
        movie.save()

        return HttpResponseRedirect(reverse("movies_detail", kwargs={"movie_id": movie_id}))
    else:
        d = movie.date_released
        date_released = f"{d.year}-{d.month:02d}-{d.day:02d}"
        print(date_released)
        context = {
            "movie" : movie,
            "date_released" : date_released
        }
        return render(request, "update.html", context)