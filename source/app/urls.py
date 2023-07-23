"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from modules import views
from modules.repository.nation.nation import (
    Nation,
    NationDetail,
)
from modules.repository.album.album import (
    Album,
    AlbumDetail,
)
from modules.repository.artist.artist import (
    Artist,
    ArtistDetail
)
from modules.repository.track.track import (
    Track,
    TrackDetail
)

urlpatterns = [
    path('api_schema', get_schema_view(title='API DOCUMENT', description='Guide for the REST API'), name='api_schema'),
    path('',
         TemplateView.as_view(
             template_name='docs.html',
             extra_context={'schema_url': 'api_schema'}
         ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('nation', Nation.as_view()),
    path('nation/<str:nation_id>/', NationDetail.as_view()),
    path('album', Album.as_view()),
    path('album/<str:album_id>/', AlbumDetail.as_view()),
    path('artist', Artist.as_view()),
    path('artist/<str:artist_id>/', ArtistDetail.as_view()),
    path('track', Track.as_view()),
    path('track/<str:artist_id>/', TrackDetail.as_view())
]
