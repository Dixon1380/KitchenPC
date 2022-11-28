
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    time_duration = models.IntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)