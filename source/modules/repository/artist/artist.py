from rest_framework.views import APIView
from rest_framework.response import Response

from modules.repository.artist.artist_serializer import ArtistSerializer
from modules.services import ArtistService


class Artist(APIView):
    def get(self, request):
        data = ArtistService.get_artist(request)
        response = ArtistSerializer(data, many=True)
        return Response(response.data)

    def post(self, request):
        artist = ArtistService.create_artist(request)
        response = ArtistSerializer(artist, many=False)
        return Response("Added successfully !")


class ArtistDetail(APIView):
    def post(self, request, album_id):
        artist = ArtistService.update_artist(request.data, album_id)
        response = ArtistSerializer(artist, many=False)
        return Response(response.data)

    def get(self, request, album_id):
        artist = ArtistService.get_artist_by_id(album_id)
        response = ArtistSerializer(artist, many=True)
        return Response(response.data)

    def put(self, request, album_id):
        artist = ArtistService.delete_artist(album_id)
        response = ArtistSerializer(artist, many=False)
        return Response(response.data)
