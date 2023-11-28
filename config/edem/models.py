from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(default='standart-1.jpg', null=True)
    description = models.TextField()
    price_uz = models.IntegerField()
    price_eu = models.IntegerField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"Image for {self.course.title}"
