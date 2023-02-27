from rest_framework.views import APIView
from rest_framework.response import Response

from modules.repository.album.album_serializer import AlbumSerializer
from modules.services import AlbumService


class Album(APIView):
    def get(self, request):
        data = AlbumService.get_album(request)
        response = AlbumSerializer(data, many=True)
        return Response(response.data)

    def post(self, request):
        nation = AlbumService.create_album(request)
        response = AlbumSerializer(nation, many=False)
        return Response("Added successfully !")


class AlbumDetail(APIView):
    def post(self, request, album_id):
        nation = AlbumService.update_album(request.data, album_id)
        response = AlbumSerializer(nation, many=False)
        return Response(response.data)

    def get(self, request, album_id):
        nation = AlbumService.get_album_by_id(album_id)
        response = AlbumSerializer(nation, many=True)
        return Response(response.data)

    def put(self, request, album_id):
        nation = AlbumService.delete_album(album_id)
        response = AlbumSerializer(nation, many=False)
        return Response(response.data)
