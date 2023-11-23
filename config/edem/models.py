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
    product = models.ForeignKey('Course', on_delete=models.CASCADE)
    # Другие поля вашего изображения

    image1 = models.ImageField(upload_to='uploads/')
    image2 = models.ImageField(upload_to='uploads/')
    image3 = models.ImageField(upload_to='uploads/')
    image4 = models.ImageField(upload_to='uploads/')
    image5 = models.ImageField(upload_to='uploads/')
    image6 = models.ImageField(upload_to='uploads/')
    image7 = models.ImageField(upload_to='uploads/')
    image8 = models.ImageField(upload_to='uploads/')

    def get_images(self):
        return [self.image1.url, self.image2.url, self.image3.url, self.image4.url, self.image5.url, self.image6.url,
                self.image7.url, self.image8.url, ]
