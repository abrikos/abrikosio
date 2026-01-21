from django.conf import settings
from django.db import models
import markdown

# Create your models here.
class Post(models.Model):
    """Post model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="post_user_set",
    )
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    short = models.TextField(max_length=500, blank=True)
    poster = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

    @property
    def markdown_body(self):
        return markdown.markdown(self.body)
    @property
    def date(self):
        return self.created_at.strftime("%Y-%m-%d, %H:%M:%S")
