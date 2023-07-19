from rest_framework.serializers import ModelSerializer
from modules.models.track.track import Track


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'