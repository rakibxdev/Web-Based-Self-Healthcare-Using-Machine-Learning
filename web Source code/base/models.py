from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=75, null=True)
    password = models.CharField(max_length=200, null=True)
    disease = models.CharField(max_length=200, null=True)