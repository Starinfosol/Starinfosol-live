# Generated by Django 3.2.3 on 2021-05-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_post_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others')], default='Technology', max_length=100),
        ),
    ]
