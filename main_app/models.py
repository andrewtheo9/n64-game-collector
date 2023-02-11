from django.db import models
from django.urls import reverse

HOURS = (
    ('1', '1 hour'),
    ('2', '2 hours'),
    ('3', '3 hours'),
    ('4', '4 hours'),
    ('5', '5 hours'),
    ('6', '6 hours'),
    ('7', '7 hours'),
    ('8', '8 hours'),
    ('9', '9 hours'),
)

# Create your models here.

class Player(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})


class N64game(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'n64game_id': self.id})

class Session(models.Model):
    date = models.DateField('Date of play session')
    hour = models.CharField(
        max_length=1,
            choices=HOURS,
            default=HOURS[0][0]
            )

    n64game = models.ForeignKey(N64game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_hour_display()} on {self.date}"

    class Meta:
        ordering = ['-date']