from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    position = models.CharField(max_length=150, blank=True, null=True, verbose_name='Должность')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.first_name else self.username
