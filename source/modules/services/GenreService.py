import datetime
from rest_framework.exceptions import ValidationError, NotFound
from modules.common.constant import PAGE_SIZE_DEFAULT
from django.core.paginator import Paginator
from modules.common import common
from modules.models.genre.genre import (
    Genre, TrackGenre
)


def get_genre(request):
    search = common.get_request(request, 'search')
    page = int(common.get_request(request, 'page')) if common.get_request(request, 'page') else 1

    if not search:
        search = ''

    query = Genre.objects.filter(name__icontains=search).order_by('name')
    paginator = Paginator(query, PAGE_SIZE_DEFAULT)
    genre = paginator.page(page)

    return genre
