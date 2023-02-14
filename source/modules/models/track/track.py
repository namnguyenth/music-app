from django.db import models

# Create your models here.


class Track(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=250, null=True)
    album_ref = models.ForeignKey('Album', null=True, on_delete=models.CASCADE)
    release_date = models.DateTimeField(null=True)
    audio_url = models.CharField(max_length=500, null=True)
    image_url = models.CharField(max_length=500, null=True)
    duration = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    type = models.IntegerField(null=True)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)