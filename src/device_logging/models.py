from django.db import models
from datetime import datetime
from ninja import Schema


class DeviceLog(models.Model):
    device = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    cause = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


class DeviceLogPost(Schema):
    device: str
    state: str
    cause: str


class DeviceLogOut(Schema):
    id: int
    device: str
    state: str
    cause: str
    timestamp: datetime
