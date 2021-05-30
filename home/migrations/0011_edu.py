# Generated by Django 3.2.3 on 2021-05-29 16:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210523_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default='blog.jpg', null=True, upload_to='images')),
                ('author', models.CharField(max_length=14)),
                ('tags', models.CharField(choices=[('Technology', 'Technology'), ('Health service', 'Health service'), ('Education', 'Education'), ('Others', 'Others')], default='Technology', max_length=100)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
