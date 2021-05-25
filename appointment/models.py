from django.db import models
from django.utils import timezone

# Create your models here.

TAGS = (('Dr. Bhuvneshwer', 'Dr. Bhuvneshwer'), ('Dr. Ishwari', 'Dr. Ishwari'), ('Dr. Shriwastav', 'Dr. Shriwastav'))


class Appointment(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    phone= models.CharField(max_length=10)
    date= models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, default="")
    department= models.CharField(max_length=255)
    doctor=models.CharField(choices=TAGS, max_length=255, default="")
    information= models.TextField()
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name