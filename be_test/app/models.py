from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
import uuid


# Create your models here.


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)


class Jobs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    type = models.CharField(max_length=50, null=True)
    url = models.URLField(null=True)
    created_at = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=255)
    company_url = models.URLField(null=True)
    location = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    how_to_apply = models.TextField(null=True)
    company_logo = models.URLField(null=True)
