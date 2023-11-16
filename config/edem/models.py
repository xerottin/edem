from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Rooms(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rooms'
