from django.db import models
from django.utils import timezone


class Riddle(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    riddle = models.TextField()
    solution = models.CharField(max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
