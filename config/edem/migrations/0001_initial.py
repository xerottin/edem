# Generated by Django 4.1.4 on 2023-11-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(null=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
    ]
