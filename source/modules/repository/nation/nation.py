from rest_framework.views import APIView
from rest_framework.response import Response

from modules.repository.nation.nation_serializer import NationSerializer
from modules.services import NationService


class Nation(APIView):
    def get(self, request):
        data = NationService.get_nation(request)
        response = NationSerializer(data, many=True)
        return Response(data=response.data)

    def post(self, request):
        nation = NationService.create_nation(request)
        response = NationSerializer(nation, many=False)
        return Response("Added successfully !")


class NationDetail(APIView):
    def post(self, request, nation_id):
        nation = NationService.update_nation(request.data, nation_id)
        response = NationSerializer(nation, many=False)
        return Response(response.data)

    def get(self, request, nation_id):
        nation = NationService.get_nation_by_id(nation_id)
        response = NationSerializer(nation, many=True)
        return Response(response.data)

    def put(self, request, nation_id):
        nation = NationService.delete_nation(nation_id)
        response = NationSerializer(nation, many=False)
        return Response(response.data)
