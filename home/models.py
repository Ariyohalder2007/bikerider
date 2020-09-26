from django.db import models
import django.utils.timezone
import datetime
mydate = django.utils.timezone.now
class Event(models.Model):
    
    heading=models.CharField(max_length=30)
    content=models.CharField(max_length=400)
    image=models.ImageField(upload_to='shop/images')
    publish_date=models.DateField(default=mydate)
    event_date=models.DateField(default=mydate)
    def __str__(self):
        return self.heading

# Create your models here.
