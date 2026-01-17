from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
import hashlib

# Create your models here.
class Manager(UserManager):
    """User manager"""

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Пользователь должен иметь email")
        user = self.model(email=email)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=email,
        )
        user.username = ""
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

def avatar_rename(instance, filename):
    return 'static/avatar/{0}.{1}'.format(hashlib.md5(b'{instance.email}').hexdigest(), filename.split('.')[1])

class User(AbstractUser):
    """User model"""

    objects = Manager()
    username = None
    email = models.EmailField(verbose_name="email", unique=True)
    avatar = models.ImageField(upload_to=avatar_rename, verbose_name="AvatarImage", null=True, blank=True)
    tg_chat_id = models.CharField(
        max_length=150, verbose_name="Telegram chat id", null=True, blank=True
    )
    country = models.CharField(
        max_length=50, verbose_name="Country", null=True, blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
