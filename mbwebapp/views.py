from django.http import HttpResponse


def index(request):
    return HttpResponse("Esse é o index principal.")
