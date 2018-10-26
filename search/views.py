from django.shortcuts import render


def hello_world(request):
    return render(request, 'search/hello_world.html')


def search(request):
    pass
