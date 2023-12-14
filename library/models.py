from django.db import models


class Book(models.Model):
    COVER_CHOICES = {
        "H": "HARD",
        "S": "SOFT"
    }
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=150)
    cover = models.CharField(max_length=1, choices=COVER_CHOICES)
    inventory = models.PositiveIntegerField()
    daily = models.DecimalField()

