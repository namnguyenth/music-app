from django.contrib import admin

from modules.models.nation.nation import Nation
from modules.models.album.album import Album
from modules.models.artist.artist import Artist

admin.site.register(
    Nation
)
admin.site.register(
    Album
)
admin.site.register(
    Artist
)