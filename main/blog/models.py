from pyexpat import model
from tkinter import CASCADE
from turtle import title
from typing import cast
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from utils import phone_validation

role_selection = (
    (1, "admin"),
    (2, "moderator"),
    (3, "gn_user"),
)


status_options = (
    (1, "active"),
    (2, "archived"),
    (3, "deleted"),
)


class Role(models.Model):
    role_name = models.PositiveBigIntegerField(
        choices=role_selection, null=True, blank=False
    )


class ManagementUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    ph_no = models.CharField(
        validators=phone_validation(), max_length=15, blank=False, null=True
    )


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=False)
    content = models.TextField(null=True, blank=True, default="")
    status = models.PositiveIntegerField(choices=status_options, blank=True, null=True)
