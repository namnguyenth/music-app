from django.db import models
from django.db.models.a import models

# Create your models here.


class Playlist(models.Model):
    id = models.AutoField(primary_key=True, null=True, unique=True)
    name = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=500, null=True)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)


class PlaylistUser(models.Model):
    id = models.AutoField(primary_key=True, null=True, unique=True)
    play_list_ref = models.ForeignKey('Playlist', null=True, on_delete=models.CASCADE)
    track_ref = models.ForeignKey('Track', null=True, on_delete=models.CASCADE)
    # user_ref = models.ForeignKey('Track', null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)


class PlaylistUser(models.Model):
    id = models.AutoField(primary_key=True, null=True, unique=True)
    play_list_ref = models.ForeignKey('Playlist', null=True, on_delete=models.CASCADE)
    track_ref = models.ForeignKey('Track', null=True, on_delete=models.CASCADE)
    # user_ref = models.ForeignKey('Track', null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)