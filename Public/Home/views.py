from django.shortcuts import render
from django_hosts import reverse

from core.Joke.models import Joke


def home_index(request):
    return render(request, 'Public/index.html')


def home_top(request):
    jokes_url = reverse('api-v1:jokes-liked-list', host='api')
    return render(request, 'Public/top.html', {'jokes_url': jokes_url})


def home_favourite(request):
    jokes_url = reverse('api-v1:jokes-favourite-list', host='api')
    return render(request, 'Public/favourite.html', {'jokes_url': jokes_url})
