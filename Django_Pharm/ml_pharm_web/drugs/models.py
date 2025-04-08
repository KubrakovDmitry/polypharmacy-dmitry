from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class DrugGroup(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название группы")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('DrugGroup', kwargs={'DrugGroup_slug': self.slug})

    class Meta:
        verbose_name = 'Группа ЛС'
        verbose_name_plural = 'Группы ЛС'
        ordering = ['title']

class Drug(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название лекарственного средства')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    pg = models.ForeignKey('DrugGroup', null=True, on_delete=models.CASCADE,
                           verbose_name='Группа лекарственных средств')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Drug', kwargs={'Drug_slug': self.slug})

    class Meta:
        verbose_name = 'ЛС'
        verbose_name_plural = 'ЛС'
        ordering = ['name']
        