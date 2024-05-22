from django.db import models


class UserRequest(models.Model):
    text = models.TextField()
