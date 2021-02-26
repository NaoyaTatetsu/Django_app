from django.contrib.auth.models import AbstractUser


class MyUserTable(AbstractUser):
    class Meta:
        verbose_name_plural = 'MyUserTable'