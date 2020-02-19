from enum import Enum

from django.db import models


class StatusChoice(Enum):
    ACTIVE = "ACTIVE"
    SUSPEND = "SUSPEND"
    CLOSE = "CLOSE"
    OTHER = "OTHER"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100)
    password = models.TextField()
    phone = models.CharField(max_length=20, null=True)
    dob = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in StatusChoice])
    user_type = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
