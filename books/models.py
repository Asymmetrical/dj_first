# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book (models.Model):

    def __str__(self):
        return self.name + " - " + self.author

    name = models.CharField(max_length = 100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length = 100)

class Johans (models.Model):
    input1 = models.CharField(max_length = 100)