from django.db import models

# Create your models here.


class Album(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=250, null=True)
    release_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=75, null=True)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=75, null=True)
    deleted_date = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=75, null=True)