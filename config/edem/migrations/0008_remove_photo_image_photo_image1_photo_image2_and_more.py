# Generated by Django 4.1.4 on 2023-11-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edem', '0007_alter_photo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='image1',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image2',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]