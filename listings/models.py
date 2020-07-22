from django.db import models
from datetime import datetime


class Listing(models.Model):
    naslov_knjige = models.CharField(max_length=100)
    ime_pisca = models.CharField(max_length=100)
    prezime_pisca = models.CharField(max_length=100)
    jezik = models.CharField(max_length=100)
    pismo = models.CharField(max_length=100)
    velicina = models.CharField(max_length=100)
    dostupno = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.naslov_knjige
