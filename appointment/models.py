from django.db import models

# Create your models here.

class Appointment(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    phone= models.CharField(max_length=10)
    date= models.DateField(auto_now=False, auto_now_add=False)
    department= models.CharField(max_length=255)
    doctor= models.CharField(max_length=255)
    information= models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name