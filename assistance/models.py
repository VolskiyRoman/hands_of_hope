# assistance/models.py

from django.db import models
from django.conf import settings
from .enums import HelpTypeEnum, HelpStatusEnum


class HelpRequest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="help_requests"
    )
    type = models.CharField(
        max_length=32,
        choices=[(tag.value, tag.name.replace('_', ' ').title()) for tag in HelpTypeEnum]
    )
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    status = models.CharField(
        max_length=32,
        choices=[(tag.value, tag.name.replace('_', ' ').title()) for tag in HelpStatusEnum],
        default=HelpStatusEnum.OPEN.value
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_type_display()} | {self.location} | {self.user.email}"


class HelpReply(models.Model):
    request = models.ForeignKey(
        HelpRequest,
        related_name="replies",
        on_delete=models.CASCADE
    )
    responder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.responder.email} on request #{self.request.id}"
