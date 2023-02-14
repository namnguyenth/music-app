from rest_framework.views import APIView
from rest_framework.response import Response

from modules.repository.nation.nation_serializer import NationSerializer
from modules.services import NationService


class Nation(APIView):
    def get(self, request):
        data = NationService.get_nation(request)
        response = NationSerializer(data, many=False)
        return Response(response.data)