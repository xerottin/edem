# Generated by Django 4.1.4 on 2023-11-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edem', '0008_remove_photo_image_photo_image1_photo_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image3',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image4',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image5',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image6',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image7',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image8',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
