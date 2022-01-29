from django.http import HttpResponse


def index(request):
    return HttpResponse("<a href='http://localhost:8000/rango/about'>Rango says hey there partner!</a>")


def about(request):
    return HttpResponse(
        "Rango says here is the about page. <a href='http://localhost:8000/rango'>Click to go back to index</a>")
