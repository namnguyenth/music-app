from rest_framework.serializers import ModelSerializer
from modules.models.album.album import Album


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'