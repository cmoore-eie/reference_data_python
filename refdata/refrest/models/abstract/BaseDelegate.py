from django.db import models


class BaseDelegate(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255, blank=True)
    locked = models.BooleanField(default=False, null=True, blank=True)
    createTime = models.DateTimeField(null=True, blank=True)
    updateTime = models.DateTimeField(null=True, blank=True)
    itemIdentifier = models.CharField(max_length=255, primary_key=True)

    class Meta:
        abstract = True
