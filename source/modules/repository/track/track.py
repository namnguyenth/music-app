from rest_framework.views import APIView
from rest_framework.response import Response

from modules.repository.track.track_serializer import TrackSerializer
from modules.services import TrackService


class Track(APIView):
    def get(self, request):
        data = TrackService.get_tracks(request)
        response = TrackSerializer(data, many=True)
        return Response(response.data)

    @staticmethod
    def post(self, request):
        track = TrackService.create_track(request)
        response = TrackSerializer(track, many=False)
        return Response("Added successfully !")


class TrackDetail(APIView):
    def post(self, request, nation_id):
        track = TrackService.update_track(request.data, nation_id)
        response = TrackSerializer(track, many=False)
        return Response(response.data)

    def get(self, request, nation_id):
        pass
        # nation = TrackService.get_nation_by_id(nation_id)
        # response = NationSerializer(nation, many=True)
        # return Response(response.data)

    def put(self, request, nation_id):
        pass
    #     nation = TrackService.delete_nation(nation_id)
    #     response = NationSerializer(nation, many=False)
    #     return Response(response.data)
