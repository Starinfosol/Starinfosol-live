# Generated by Django 3.2.3 on 2021-05-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_auto_20210526_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(),
        ),
    ]