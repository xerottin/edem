from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()
    description = models.TextField()
    price_uz = models.IntegerField()
    price_eu = models.IntegerField()

    def __str__(self):
        return self.title
