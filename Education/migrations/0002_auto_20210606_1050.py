# Generated by Django 3.2.3 on 2021-06-06 05:20

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='image',
        ),
        migrations.AddField(
            model_name='education',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=''),
        ),
    ]