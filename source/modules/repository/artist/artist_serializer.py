from rest_framework.serializers import ModelSerializer
from modules.models.artist.artist import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'