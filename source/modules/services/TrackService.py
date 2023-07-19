import datetime

from django.db.models import Q

from modules.common import common
from modules.models.track.track import Track
from modules.models.artist.artist import TrackArtist


def get_tracks(request):
    search = common.get_request(request, 'search')
    if not search:
        search = ''

    tracks = TrackArtist.objects.select_related('track_ref')

    response = [
        {
            "id": track.track_ref.id,
            "name": track.track_ref.name,
        } for track in tracks
    ]

    return response


def create_track(request):
    track = Track.objects.create(
        name=request.data['name'],
        created_date=datetime.datetime.now(),
        created_by='admin',
        updated_date=datetime.datetime.now(),
        updated_by='admin',
    )
    return track


def update_track(request, track_id):
    track = Track.objects.get(id=track_id)

    track.name = request['name']
    track.updated_date = datetime.datetime.now()
    track.updated_by = 'admin'

    track.save()

    return track


def get_track_by_id(track_id):
    track = Track.objects.filter(
        id__icontains=track_id,
        deleted_by__isnull=True,
        deleted_date__isnull=True,
    )
    return track


def delete_album(track_id):
    track = Track.objects.get(id=track_id)

    track.deleted_date = datetime.datetime.now()
    track.deleted_by = 'admin'

    track.save()

    return track
