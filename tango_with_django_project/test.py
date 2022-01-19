from django.http import HttpResponse


def index(request):
    return HttpResponse("Main says hey there partner!")
