from django.db import models

# Create your models here.


class Follower(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    artist_ref = models.ForeignKey('Artist', null=True, on_delete=models.CASCADE)
    # user_ref = models.ForeignKey('track', null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)