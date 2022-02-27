from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Grade(models.Model):
    number = models.IntegerField()
    letter = models.CharField(max_length=1)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='grades')
