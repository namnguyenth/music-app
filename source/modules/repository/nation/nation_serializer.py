from rest_framework.serializers import ModelSerializer
from modules.models.nation.nation import Nation


class NationSerializer(ModelSerializer):
    class Meta:
        model = Nation
        fields = '__all__'