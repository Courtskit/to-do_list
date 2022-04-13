from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    name = models.CharField(max_length=64)
    date = models.DateField()

    def __str__(self):
        return self.name


class ListItem(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=250)
    list_name = models.ForeignKey(List, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name