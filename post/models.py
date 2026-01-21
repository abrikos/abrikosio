from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
import markdown

class Test:
    title = models.CharField(max_length=255, blank=True)

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

def validate_not_zero(value):
    if value == 0:
        raise ValidationError(
            'Wrong value %(value)s',
            params={'value': value},
        )

class Rate(models.Model):
    """Rate model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rate_user_set",
    )
    post = models.ForeignKey(
        Post,
        related_name="rate_post_set",
        on_delete=models.CASCADE,
    )
    value = models.IntegerField(default=0, validators=[validate_not_zero])

