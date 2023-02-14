from django.db import models

# Create your models here.


class Artist(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=250, null=True)
    birth_date = models.DateTimeField(null=True)
    nation_ref = models.ForeignKey('Nation', null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)


class TrackArtist(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    track_ref = models.ForeignKey('Track', null=True, on_delete=models.CASCADE)
    artist_ref = models.ForeignKey('Artist', null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)