from django.db import models


# Create your models here.
class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title