from django.db import models
from django.urls import reverse

# Create your models here.

class N64game(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'n64game_id': self.id})