from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='movie/images/')
    showtime_1 = models.DateTimeField(default=datetime.now)
    showtime_2 = models.DateTimeField(default=datetime.now)
    showtime_3 = models.DateTimeField(default=datetime.now)
    showtime_4 = models.DateTimeField(default=datetime.now)
    showtime_5 = models.DateTimeField(default=datetime.now)
    showtime_6 = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    upcoming = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[('coming_soon', 'Coming Soon'), ('currently_playing', 'Currently Playing')], default='coming_soon')
    runtime = models.IntegerField(blank=True, null=True)
    cast = models.CharField(max_length=500, blank=True)

class Review(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
