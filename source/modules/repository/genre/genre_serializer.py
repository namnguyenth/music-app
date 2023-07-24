from rest_framework.serializers import ModelSerializer
from modules.models.genre.genre import Genre


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'