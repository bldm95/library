import os

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    year_of_publication = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000, blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    # При blank=True, проверка данных в форме позволит сохранять пустое значение в поле

    def __str__(self):
        return self.author + ' ' + self.name
