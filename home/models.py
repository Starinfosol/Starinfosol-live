from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.timezone import now

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=100)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp= models.DateTimeField(auto_now_add=True, blank=True)
     is_deleted=models.BooleanField(default=False)
     created_at = models.DateField(auto_now_add=True, blank=True, null=True)

     def __str__(self):
        return self.name



