from django.db import models

# Create your models here.

# Allow Genre class to inherit Model class from models module


class Genre(models.Model):
    # No genre name cannot have more than 255 characters
    name = models.CharField(max_length=255)


# Create attributes for movies
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # connect (create "relationship") between Movie and Genre
    # on_delete = when genre deleted, all movies associated also deleted ("cascading")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
