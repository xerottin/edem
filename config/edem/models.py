from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(default='standart-1.jpg', null=True)
    description = models.TextField()
    price_uz = models.IntegerField()
    price_eu = models.IntegerField()
    size_room = models.TextField()
    beds = models.TextField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:120] + ' ...'


class Photo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(default='standart-1.jpg', null=True)

    def __str__(self):
        return f"Image for {self.course.title}"
