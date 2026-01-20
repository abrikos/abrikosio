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
    return f'static/avatar/{hashlib.md5(instance.email.encode()).hexdigest()}'

class User(AbstractUser):
    """User model"""

    objects = Manager()
    username = None
    email = models.EmailField(verbose_name="email", unique=True)
    avatar = models.ImageField(upload_to=avatar_rename, verbose_name="AvatarImage", null=True, blank=True)
    tg_chat_id = models.CharField(max_length=150, verbose_name="Telegram chat id", null=True, blank=True)
    nickname = models.CharField(max_length=150, verbose_name="Nickname", null=True, blank=True)
    publisher = models.BooleanField(verbose_name="Is publisher", default=False )

    @property
    def display_name(self):
        if self.first_name or self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
