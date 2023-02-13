# Generated by Django 4.1.2 on 2023-02-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('release_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
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
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('release_date', models.DateTimeField(null=True)),
                ('audio_url', models.CharField(max_length=500, null=True)),
                ('image_url', models.CharField(max_length=500, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('type', models.IntegerField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
                ('album_ref',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.album')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('birth_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=75, null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=75, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('deleted_by', models.CharField(max_length=75, null=True)),
                ('nation_ref',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.nation')),
            ],
        ),
    ]
