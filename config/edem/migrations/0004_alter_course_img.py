# Generated by Django 4.1.4 on 2023-11-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edem', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(default='standart-1.jpg', null=True, upload_to=''),
        ),
    ]
