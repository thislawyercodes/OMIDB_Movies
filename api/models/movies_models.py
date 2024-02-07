from django.db import models
from .base_models import BaseModel

class Movie(BaseModel):
    title = models.CharField(max_length=255)
    year_start = models.IntegerField(null=True)
    year_end = models.IntegerField(null=True)
    rated = models.CharField(max_length=10)
    released = models.DateField(null=True)
    runtime = models.IntegerField(null=True)
    plot = models.TextField(null=True)
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    awards = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=255)
    metascore = models.IntegerField(null=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    imdb_votes = models.IntegerField(null=True)
    imdb_id = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20,null=True)
    total_seasons = models.IntegerField(null=True)
    response = models.BooleanField(default=False)

    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    writers = models.ManyToManyField('Writer')
    actors = models.ManyToManyField('Actor')
    ratings = models.ManyToManyField('Rating')
    genres = models.ManyToManyField('Genre')

class Director(BaseModel):
    name = models.CharField(max_length=255)

class Writer(BaseModel):
    name = models.CharField(max_length=255)

class Actor(BaseModel):
    name = models.CharField(max_length=255)

class Rating(BaseModel):
    source = models.CharField(max_length=255)
    value = models.CharField(max_length=10)

class Genre(BaseModel):
    name = models.CharField(max_length=255)
