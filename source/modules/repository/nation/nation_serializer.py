from rest_framework import serializers

from modules.models.nation.nation import Nation


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = '__all__'