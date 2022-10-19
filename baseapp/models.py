from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.IntegerField()
    msg = models.TextField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name
