from django.shortcuts import render


def google_login(request):
    """ Cтраница входа через Гугл"""

    return render(request, 'oauth/google_login.html')