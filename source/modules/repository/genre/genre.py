from rest_framework.views import APIView
from rest_framework.response import Response

from modules.repository.genre.genre_serializer import GenreSerializer
from modules.services import GenreService


class Genre(APIView):
    def get(self, request):
        data = GenreService.get_genre(request)
        response = GenreSerializer(data, many=True)
        return Response(response.data)

    def post(self, request):
        artist = GenreService.create_artist(request)
        response = GenreSerializer(artist, many=False)
        return Response("Added successfully !")


class GenreDetail(APIView):
    def post(self, request, album_id):
        artist = GenreService.update_artist(request.data, album_id)
        response = GenreSerializer(artist, many=False)
        return Response(response.data)

    def get(self, request, album_id):
        artist = GenreService.get_artist_by_id(album_id)
        response = GenreSerializer(artist, many=True)
        return Response(response.data)

    def put(self, request, album_id):
        artist = GenreService.delete_artist(album_id)
        response = GenreSerializer(artist, many=False)
        return Response(response.data)


