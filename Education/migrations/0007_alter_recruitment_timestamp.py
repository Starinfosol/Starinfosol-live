# Generated by Django 3.2.3 on 2021-06-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0006_alter_recruitment_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=''),
        ),
    ]
