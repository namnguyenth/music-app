# Generated by Django 4.1.6 on 2023-02-14 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackGenre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
                ('genre_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.genre')),
                ('track_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.track')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
                ('play_list_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.playlist')),
                ('track_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.track')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistSystem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
                ('play_list_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.playlist')),
                ('track_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.track')),
            ],
        ),
    ]
