import datetime

from django.db.models import Q

from modules.common import common
from modules.models.album.album import Album


def get_album(request):
    search = common.get_request(request, 'search')
    if not search:
        search = ''

    album = Album.objects.filter(
        Q(name__icontains=search)
    )
    return album


def create_album(request):
    album = Album.objects.create(
        name=request.data['name'],
        created_date=datetime.datetime.now(),
        created_by='admin',
        updated_date=datetime.datetime.now(),
        updated_by='admin',
    )
    return album


def update_album(request, album_id):
    album = Album.objects.get(id=album_id)

    album.name = request['name']
    album.updated_date = datetime.datetime.now()
    album.updated_by = 'admin'

    album.save()

    return album


def get_album_by_id(album_id):
    album = Album.objects.filter(
        id__icontains=album_id,
        deleted_by__isnull=True,
        deleted_date__isnull=True,
    )
    return album


def delete_album(album_id):
    album = Album.objects.get(id=album_id)

    album.deleted_date = datetime.datetime.now()
    album.deleted_by = 'admin'

    album.save()

    return album
