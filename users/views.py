from django.shortcuts import render


def user_home(request):
    return render(request, 'users/user_home.html')
