# Generated by Django 3.2.3 on 2021-06-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0005_auto_20210606_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='upload_file',
            field=models.FileField(upload_to=''),
        ),
    ]
