# Generated by Django 3.2.3 on 2021-06-12 03:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0010_delete_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
