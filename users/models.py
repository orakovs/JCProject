from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass #добавить дополнительные поля для Юзера

    def __str__(self):
        return self.username
    