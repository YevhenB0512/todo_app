from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Задание')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    complete = models.BooleanField(default=False, verbose_name='Выполнено')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True,
                             verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        ordering = ['complete']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'