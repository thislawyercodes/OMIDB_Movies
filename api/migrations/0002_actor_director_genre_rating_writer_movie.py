# Generated by Django 5.0.2 on 2024-02-07 18:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('source', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('year_start', models.IntegerField(null=True)),
                ('year_end', models.IntegerField(null=True)),
                ('rated', models.CharField(max_length=10)),
                ('released', models.DateField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('plot', models.TextField(null=True)),
                ('language', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('awards', models.CharField(max_length=255)),
                ('poster_url', models.URLField(max_length=255)),
                ('metascore', models.IntegerField(null=True)),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('imdb_votes', models.IntegerField(null=True)),
                ('imdb_id', models.CharField(max_length=20, unique=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('total_seasons', models.IntegerField(null=True)),
                ('response', models.BooleanField(default=False)),
                ('actors', models.ManyToManyField(to='api.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.director')),
                ('genres', models.ManyToManyField(to='api.genre')),
                ('ratings', models.ManyToManyField(to='api.rating')),
                ('writers', models.ManyToManyField(to='api.writer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]