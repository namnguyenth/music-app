import datetime

from django.db.models import Q

from modules.common import common
from modules.models.nation.nation import Nation
from modules.models.artist.artist import Artist


def get_artist(request):
    search = common.get_request(request, 'search')
    if not search:
        search = ''

    artist = Artist.objects.filter(
        Q(name__icontains=search)
    )

    for a in artist:
        a

    # nation1 = Nation.objects.raw('SELECT * FROM modules_artist')
    return artist


def create_artist(request):
    artist = Artist.objects.create(
        name=request.data['name'],
        birth_date=request.data['birth_date'],
        nation_ref=int(request.data['nation_ref']),
        created_date=datetime.datetime.now(),
        created_by='admin',
        updated_date=datetime.datetime.now(),
        updated_by='admin',
    )
    return artist


def update_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)

    artist.name = request['name']
    artist.birth_date = request.data['birth_date'],
    artist.nation_ref = int(request.data['nation_ref']),
    artist.updated_date = datetime.datetime.now()
    artist.updated_by = 'admin'

    artist.save()

    return artist


def get_artist_by_id(artist_id):
    artist = Artist.objects.filter(
        id__icontains=artist_id,
        deleted_by__isnull=True,
        deleted_date__isnull=True,
    )
    return artist


def delete_artist(artist_id):
    artist = Artist.objects.get(id=artist_id)

    artist.deleted_date = datetime.datetime.now()
    artist.deleted_by = 'admin'

    artist.save()

    return artist
