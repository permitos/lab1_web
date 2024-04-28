from django.db import models
from django.utils import timezone
import datetime

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    public_date = models.DateTimeField("date published")
    image = models.ImageField()
    actual_status = True
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.public_date <= now